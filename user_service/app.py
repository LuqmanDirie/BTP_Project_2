from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse
from db import create_user, get_user_by_id, update_user, delete_user
import hashlib

class UserHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _parse_data(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        return post_data
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
    
        if len(path_parts) == 2 and path_parts[0] == 'users':
            user_id = int(path_parts[1])
            user = get_user_by_id(user_id)
            self._set_headers(200 if user else 404)
            response_data = json.dumps(user if user else {}).encode('utf-8')
            self.wfile.write(response_data)
        else:
            self._set_headers(404)
            response_data = json.dumps({'error': 'Not found'}).encode('utf-8')
            self.wfile.write(response_data)

    def do_POST(self):
        if self.path.endswith('/users'):
            data = self._parse_data()
            hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()

            user_id = create_user(data['username'], data['email'], hashed_password, data['user_type'])
            if user_id:
                self._set_headers(201)
                self.wfile.write(json.dumps({'user_id': user_id}).encode())
            else:
                self._set_headers(500)
                self.wfile.write(json.dumps({'error': 'User could not be created'}).encode())

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')

        if len(path_parts) == 2 and path_parts[0] == 'users':
            user_id = int(path_parts[1])
            data = self._parse_data()
            success = update_user(user_id, data['username'], data['email'], data['password'], data['user_type'])
            self._set_headers(200 if success else 404)
            self.wfile.write(json.dumps({'success': success}).encode())

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')

        if len(path_parts) == 2 and path_parts[0] == 'users':
            user_id = int(path_parts[1])
            success = delete_user(user_id)
            self._set_headers(200 if success else 404)
            self.wfile.write(json.dumps({'success': success}).encode())

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())

def run(server_class=HTTPServer, handler_class=UserHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server starting on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
