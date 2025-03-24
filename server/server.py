from http.server import BaseHTTPRequestHandler, HTTPServer

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/ping":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"pong")
        else:
            self.send_error(404, "Not Found")

def run():
    server_address = ('', 9000)
    httpd = HTTPServer(server_address, PingHandler)
    print("HTTP Server running on port 9000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
