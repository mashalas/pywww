#!/usr/bin/python3

# https://python-course.readthedocs.io/projects/year2/en/latest/lessons/07-simple-http-server.html

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
#import requests
from urllib.parse import urlparse, parse_qs

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        #self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())
        self.wfile.write('<body>'.encode())
        A = parse_qs(urlparse(self.path).query)
        self.wfile.write('<p>dsfsdfgsdg{}</p>'.format(A).encode())
        self.wfile.write('</body></html>'.encode())
        
    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        field_data = self.rfile.read(length)
        fields = urlparse.parse_qs(field_data)
        

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()

run(handler_class=HttpGetHandler)
