# mock_api

## Project Overview
My goal was to create a simple mock API for testing purposes and deploy it with Render.com. To achieve this, I created a database file containing the API data as well as a small backend for deployment. Additionally, I implemented API key authentication to test this functionality in other projects.

## Key Learnings
### From `http.server` to Flask
The Python module `http.server`, which was previously used in this project for server functionality, is not recommended for production due to its limitations and lack of security features. It only implements basic security checks. Therefore, I transitioned to using the Flask framework for the final version of my mock API.

### Python Decorators
I took the time to learn how Python decorators work and how to use them to better understand the construction of a Flask server.

### Deployment on Render.com
I deployed this project with Render.com. Here you can access the mock data using the following API endpoint and API key: 

[https://mock-api-books-1dn8.onrender.com/?api_key=my_supersecret_api_key](https://mock-api-books-1dn8.onrender.com/?api_key=my_supersecret_api_key)

If you use the URL without adding the (correct) API-key, you will receive an error message with the content `"error": "Invalid API key,"`. This indicates that the API authentication works correctly. You can test the response without providing any API key here:

[https://mock-api-books-1dn8.onrender.com/](https://mock-api-books-1dn8.onrender.com/). 

