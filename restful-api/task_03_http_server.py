#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # / endpoint
        if self.path == '/':
            response = "Hello, this is a simple API!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()
            self.wfile.write(response.encode())

        # /data endpoint
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()
            self.wfile.write(response.encode())

        # /status endpoint
        elif self.path == '/status':
            response = json.dumps({"status": "OK"}, separators=(',', ':'), ensure_ascii=False)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()
            self.wfile.write(response.encode())

        # /info endpoint
        elif self.path == '/info':
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            response = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()
            self.wfile.write(response.encode())

        # 404 handler
        else:
            response = json.dumps({"error": "Not found"}, separators=(',', ':'), ensure_ascii=False)
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response.encode())))
            self.end_headers()
            self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    print(f"Starting server at http://localhost:{port}")
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
