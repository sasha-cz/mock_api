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

# When the script is executed directly, we want to get hold of the port number of the hosting environment (e.g., PaaS like Heroku). 
# the port variable is set to the value of the 'PORT' environment variable if it exists. 
# If the 'PORT' environment variable is not set, it defaults to 3000.
# Additionaly, a server_adress gets configured, so the server will listen to all available network interfaces and the retrieved port number.
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000)) 
    server_adress = ("", port)

# Create an HTTP server, print a message indicating that the server is starting, and then start the server to listen for incoming HTTP requests continuously.
    with HTTPServer(server_adress, MyServer) as httpd:
        print(f"Starting server on port {port}")
        httpd.serve_forever()