#!python
"""
This holds the code responsible for running a base http server
"""

from http import server
import threading
import webbrowser
import sys
import urllib
import subnet_calculator

__author__ = "Alex DeCesare"
__version__ = "11-October-2020"

MAX_URL_QUERIES = 2

def run():
    """
    runs the http server
    """
    ip_address = 'localhost'
    port = 3280
    handler = generate_handler()

    srv = server.HTTPServer((ip_address, port), handler)
    sys.stdout.flush()

    def start_browser():
        """
        opens the browser
        """
        return webbrowser.open('http://{}:{}'.format(ip_address, port))
    threading.Thread(target=start_browser).start()

    try:
        srv.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        print('stopped server')

    srv.server_close()
def generate_handler():
    """
    generates the http handler
    """
    class Handler(server.BaseHTTPRequestHandler):
        """
        The base http request header
        """
        def do_GET(self):
            """
            sets the information for the GET request
            """

            url = urllib.parse.urlparse(self.path)
            url_queries = url.query.split('&')

            valid_path = '/subnet?' + url_queries[0] + '&' + url_queries[1]
            if ((len(url_queries) == MAX_URL_QUERIES) and (self.path == valid_path)):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ip_address = url_queries[0]
                subnet_mask = url_queries[1]
                html = set_ip_html_information(ip_address, subnet_mask)
                self.wfile.write(html.encode())
            elif not self.path.startswith('/subnet?'):
                self.send_response(404)
            else:
                self.send_error(400)
    return Handler

def set_ip_html_information(ip_address, subnet_mask):
    """
    sets the ip information for display on the webpage
    """
    html = ''

    if subnet_calculator.validate_ipv4_address(ip_address):
        html += '<p>ipv4 address: ' + ip_address + '\n<p>'

        if subnet_calculator.validate_ipv4_netmask_as_ip(subnet_mask):
            subnet = subnet_calculator.calculate_ipv4_subnet(ip_address, subnet_mask)
            lower_range = subnet_calculator.calculate_lower_ipv4_range(ip_address, subnet_mask)
            upper_range = subnet_calculator.calculate_upper_ipv4_range(ip_address, subnet_mask)

            html += '<p>subnet mask: ' + subnet_mask + '\n</p>'
            html += '<p>ipv4 subnet: ' + subnet + '\n</p>'
            html += '<p>ipv4 range: ' + lower_range + ' - ' + upper_range + '\n</p>'
        elif subnet_calculator.validate_ipv4_netmask_as_bit(subnet_mask):
            binary_mask = subnet_calculator.convert_netmask_bits_to_binary(subnet_mask, 35, 9)
            subnet = subnet_calculator.calculate_ipv4_subnet(ip_address, binary_mask)
            lower_range = subnet_calculator.calculate_lower_ipv4_range(ip_address, binary_mask)
            upper_range = subnet_calculator.calculate_upper_ipv4_range(ip_address, binary_mask)

            html += '<p>subnet mask: ' + subnet_mask + '\n</p>'
            html += '<p>ipv4 subnet: ' + subnet + '\n</p>'
            html += '<p>ipv4 range: ' + lower_range + ' - ' + upper_range + '\n</p>'

        else:
            html += '<p>invalid net mask, enter a netmask in either ipv4 or bit format\n</p>'
    elif subnet_calculator.validate_ipv6_address(ip_address):
        html += '<p>ipv6 address: ' + ip_address + '\n</p>'

        if subnet_calculator.validate_ipv6_netmask_as_bit(subnet_mask):
            binary_mask = subnet_calculator.convert_netmask_bits_to_binary(subnet_mask, 135, 17)
            subnet = subnet_calculator.calculate_ipv6_subnet(ip_address, binary_mask)
            lower_range = subnet_calculator.calculate_lower_ipv6_range(ip_address, binary_mask)
            upper_range = subnet_calculator.calculate_upper_ipv6_range(ip_address, binary_mask)

            html += '<p>subnet mask: ' + subnet_mask + '\n</p>'
            html += '<p>ipv6 subnet: ' + subnet + '\n</p>'
            html += '<p>ipv6 range: ' + lower_range + ' - ' + upper_range + '\n</p>'
        else:
            html += '<p>invalid netmask, please enter a netmask in bit format\n</p>'
    else:
        html += '<p>invalid ip address, please enter an address in ipv4 or ipv6 format\n</p>'

    return html

if __name__ == '__main__':
    run()
