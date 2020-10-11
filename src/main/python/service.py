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
lower_ip_range = ''
upper_ip_range = 'dd'

def run(html,http_server = None, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    
    ip = 'localhost'
    port = 3280
    open_browser = True
    subnet = {'size' : '600x400'}
    Handler = generate_handler(html)
    print(type(Handler))

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

    if files is None:
        files = {}

    class Handler(server.BaseHTTPRequestHandler):

        def do_GET(self):

            url = urllib.parse.urlparse(self.path)
            url_queries = url.query.split('&')

            if ((len(url_queries) == MAX_URL_QUERIES) and (self.path == '/subnet?' + url_queries[0] + '&' + url_queries[1])):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode())
                print('ran')
            elif (self.path.startswith('/subnet?') == False):
                self.send_response(404)
            else:
                self.send_error(400)
    return Handler


if (__name__ == '__main__'):
    run('<h1>hello world' + upper_ip_range + '</h1>')
