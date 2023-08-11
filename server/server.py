from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver

PORT = 8468

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("Got a GET Request", str(self.path), str(self.headers))
        self._set_headers()
        self.wfile.write("You sent a GET Request, Hello mate\n".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Server, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        print("Attempting to start server")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    print("Closing server")
    httpd.server_close()

if __name__ == '__main__':
    run()
