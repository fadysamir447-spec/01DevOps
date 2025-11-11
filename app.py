from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Tekton + Kaniko + Helm! this is a test 1\n")

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

