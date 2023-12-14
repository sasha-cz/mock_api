from flask import Flask, jsonify, request
import os

#The app object is declared by the Flask class.
app = Flask(__name__)

# Import the 'mock_api' data from the 'db' module representing your database.
from db import data

# Retrieve the API key from the environment variable.
API_KEY = os.environ.get("API_KEY")

# Set up API Endpoint: Use the decorator function 'route' from the Flask app object to set the root path and implement API key authentication. 
@app.route("/", methods=["GET"])
def index():
    api_key = request.args.get("api_key")
    if request.method=="GET":
        if api_key is None or api_key != API_KEY:
            return jsonify({"error": "Invalid API key"}), 401
# Serialize data to json format and create a JSON response.
        return jsonify(data)
    
# Run the Flask development server on all available network interfaces with debugging turned off,
# suitable for deployment on platforms like Render.com.
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 3000))) 
