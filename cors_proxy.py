from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

url = 'http://localhost:8501/v1/models/default:predict'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = requests.post(url, data=body)

        self.wfile.write(response.content)

httpd = HTTPServer(('localhost', 8502), SimpleHTTPRequestHandler)
httpd.serve_forever()