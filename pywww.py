#!/usr/bin/python3

# https://andreyex.ru/python-3/python-davajte-sozdadim-prostoj-http-server/

import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# python -m http.server 8080 --bind 127.0.0.1
