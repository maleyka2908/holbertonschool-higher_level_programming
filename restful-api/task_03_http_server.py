#!/usr/bin/python3
"""
Python-un http.server modulu ilə sadə bir API server.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP GET sorğularını idarə edən class.
    """

    def do_GET(self):
        """GET sorğularını endpoint-lərə görə yönləndirir."""
        
        # 1. Əsas səhifə (Root)
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. /data endpoint-i (JSON qaytarır)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        # 3. /status endpoint-i
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. /info endpoint-i
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        # 5. Tapılmayan endpoint-lər (404 Error)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server():
    """Serveri 8000 portunda başladır."""
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server 8000 portunda işləyir...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
