# A simple HTTP server (MyServer) using Python's http.server module, responding with mock API data in JSON format for requests to "/mock_api/books".
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from db import mock_api
import os

# Make a class to handle HTTP requests.
class MyServer(BaseHTTPRequestHandler):
# The do_GET method is a special method in the BaseHTTPRequestHandler class. It is called when an HTTP GET request is received.
    def do_GET(self):
        if self.path == "/mock_api/books":
            self.send_response(200)
# the Content-type header indicates the type of data that is being sent in the body of the response. It tells the client (e.g., the browser) how to interpret the data.
# 'application/json' is the value associated with the Content-type header. In this case, it specifies that the content of the response is in JSON format.
            self.send_header("Content-type", "application/json")
            self.end_headers()

# Convert data to JSON format
            response = json.dumps(mock_api).encode("utf-8")
# Send the HTTP response body to the client
            self.wfile.write(response)

# Create a Server, that listens for incoming HTTP requests continuously. 
if __name__ == "__main__":
    serverPort = int(os.environ.get("PORT", 3000)) 
    webServer = HTTPServer(("", serverPort), MyServer)
    print(f"Starting server on port {serverPort}")
    webServer.serve_forever()
