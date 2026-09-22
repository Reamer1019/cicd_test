from http.server import BaseHTTPRequestHandler, HTTPServer

from app import add


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"1 + 2 = {add(1, 2)}\n".encode())

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
