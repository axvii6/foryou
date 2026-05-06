from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == "__main__":
    print(f"🌸 Server running on http://localhost:{PORT}")
    print("Press CTRL+C to stop the server.")
    with HTTPServer(("", PORT), CustomHandler) as httpd:
        httpd.serve_forever()
