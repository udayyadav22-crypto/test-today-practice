from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            status = 200
            response = {"status": "healthy"}
        elif self.path == "/":
            status = 200
            response = {"message": "DevOps CI/CD Practice App"}
        else:
            status = 404
            response = {"error": "Not found"}

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
