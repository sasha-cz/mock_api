from flask import Flask, jsonify, request
import os

#The app object is declared by the Flask class.
app = Flask(__name__)

# Import the 'mock_api' data from the 'db' module representing your database.
from db import mock_api

# Use the decorator function 'route' from the Flask app object to define a route for the '/mock-api/books' URL
@app.route("/", methods=["GET"])
def index():
    if request.method=="GET":
# Serialize mock_api to json format and create a JSON response
        return jsonify(mock_api)
# Run the Flask development server on all available network interfaces with debugging turned off,
# suitable for deployment on platforms like Render.com
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 3000))) 
