#!/usr/bin/env python3
"""
Simple HTTP server using Python's built-in http.server module.

This server handles basic GET requests for a few fixed routes:
- "/"          : returns a greeting message.
- "/data"      : returns some example user data in JSON format.
- "/status"    : returns a simple OK status.
- "/info"      : returns version and description of the API.

If a user accesses any other route, the server will return a 404 error.
"""

import http.server
import socketserver
import json

# Custom request handler
class Server(http.server.BaseHTTPRequestHandler):
    """
    Handles HTTP GET requests and responds with data based on the requested path.
    """

    def do_GET(self):
        """
        Responds to GET requests:
        - '/' returns a greeting message.
        - '/data' returns a JSON with name, age, city.
        - '/status' returns 'OK'.
        - '/info' returns API version and description.
        - any other path returns a 404 error with a custom message.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode("utf-8"))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))

# Start the server on port 8000
if __name__ == "__main__":
    with socketserver.TCPServer(('', 8000), Server) as httpd:
        print("Starting server at http://localhost:8000")
        httpd.serve_forever()
