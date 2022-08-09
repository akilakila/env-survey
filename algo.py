from http.server import *
import os
import sys
import subprocess
import json

class Server(BaseHTTPRequestHandler):
    # Helper function for retrieving input
    def get_body(self):
        content_len_header = self.headers.get("Content-Length")
        content_len = 0
        if content_len_header is not None:
            content_len = int(content_len_header)
        return self.rfile.read(content_len)

    # Method for pre-processing of the server
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        openFile = open(self.path[1:]).read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(openFile, 'utf-8'))

    # What happens once we do the fetch method
    # For now, the values are stored in dict
    # You guys can handle the algo stuff :)
    def do_POST(self):
        input = self.get_body()
        dict = json.loads(input)

        #converts the strings from the dict into ints
        sum = 0
        for key in dict:
            num = int(dict[key])
            sum += num
        sum = sum//5
        print(sum)
        if sum < 2:
            print("category 1")
        elif sum == 3:
            print("category 2")
        elif sum == 4:
            print("category 3")
        elif sum == 5:
            print("category 4")
        else:
            print("error")

# These two lines we'll need to create/use the server
httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()