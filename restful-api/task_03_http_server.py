#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Set base status and headers
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            status = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status).encode())

        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error = {
                "error": "Endpoint not found"
            }
            self.wfile.write(json.dumps(error).encode())

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
