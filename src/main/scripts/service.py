#!/usr/bin/env python3
"""
This holds the code responsible for running a base http server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from http import server
import threading
import webbrowser
import sys
import subnet_calculator
import urllib

__author__ = "Alex DeCesare"
__version__ = "11-October-2020"

MAX_URL_QUERIES = 2
ip_address = ''
subnet_mask = ''
lower_ip_range = ''
upper_ip_range = ''
subnet = ''

def run(html,http_server = None, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """
    runs the http server
    """
    ip = 'localhost'
    port = 3280
    open_browser = True
    Handler = generate_handler(html)

    srv = server.HTTPServer((ip, port), Handler)
    sys.stdout.flush()

    def b():
        return webbrowser.open('http://{}:{}'.format(ip, port))
    threading.Thread(target=b).start()
        
    try:
        srv.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        print('stopped server')

    srv.server_close()
def generate_handler(html, files=None):
    """
    generates the http handler
    """

    if files is None:
        files = {}

    class Handler(server.BaseHTTPRequestHandler):

        def do_GET(self):
            """
            sets the information for the GET request
            """

            url = urllib.parse.urlparse(self.path)
            url_queries = url.query.split('&')

            if ((len(url_queries) == MAX_URL_QUERIES) and (self.path == '/subnet?' + url_queries[0] + '&' + url_queries[1])):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                ip_address = url_queries[0]
                subnet_mask = url_queries[1]
                html = set_ip_html_information(ip_address, subnet_mask)
                self.wfile.write(html.encode())
            elif (self.path.startswith('/subnet?') == False):
                self.send_response(404)
            else:
                self.send_error(400)
    return Handler

def set_ip_html_information(ip_address, subnet_mask):
    """
    sets the ip information for display on the webpage
    """
    html = ''

    if(subnet_calculator.validate_ipv4_address(ip_address)):
        html += '<p>ipv4 address: ' + ip_address + '\n<p>'

        if(subnet_calculator.validate_ipv4_netmask_ip_format(subnet_mask)):
            html += '<p>subnet mask: ' + subnet_mask + '\n</p>'
            html += '<p>ipv4 subnet: ' + subnet_calculator.calculate_ipv4_subnet(ip_address, subnet_mask) + '\n</p>'
            html += '<p>ipv4 range: ' + subnet_calculator.calculate_upper_ipv4_range(ip_address, subnet_mask) + '\n</p>'
        elif (subnet_calculator.validate_ipv4_netmask_bit_format(subnet_mask)):
            html += '<p>subnet mask: ' + subnet_mask + '\n</p>'
            binary_mask = subnet_calculator.convert_netmask_bits_to_binary(subnet_mask, 35, 9)
            html += '<p>ipv4 subnet: ' + subnet_calculator.calculate_ipv4_subnet(ip_address, binary_mask) + '\n</p>'
            html += '<p>ipv4 range: ' + subnet_calculator.calculate_upper_ipv4_range(ip_address, binary_mask) + '\n</p>'
        else:
            html += '<p>invalid net mask, please enter a netmask in either an ipv4 format or a bit format\n</p>'
    elif(subnet_calculator.validate_ipv6_address(ip_address)):
        html += '<p>ipv6 address: ' + ip_address + '\n</p>'

        if(subnet_calculator.validate_ipv6_netmask_bit_format(subnet_mask)):
            html +='<p>subnet mask: ' + subnet_mask + '\n</p>'
            binary_mask = subnet_calculator.convert_netmask_bits_to_binary(subnet_mask, 135, 17)
            html += '<p>ipv6 subnet: ' + subnet_calculator.calculate_ipv6_subnet(ip_address, binary_mask) + '\n</p>'
            html += '<p>ipv6 range: ' + subnet_calculator.calculate_upper_ipv6_range(ip_address, binary_mask) + '\n</p>'
        else:
            html += '<p>invalid netmask, please enter a netmask in bit format\n</p>'
    else:
        html += '<p>invalid ip address, please enter an address in ipv4 or ipv6 format\n</p>'

    return html

if (__name__ == '__main__'):
    run('<h1>h</h1>')
