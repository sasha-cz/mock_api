# mock_api

## Project Overview
My goal was to create a simple mock API for testing purposes and deploy it. To achieve this, I created a database file containing the API data as well as a small backend for deployment.

## Key Learnings
### From `http.server` to Flask
The Python module `http.server`, which was previously used in this project for server functionality, is not recommended for production due to its limitations and lack of security features. It only implements basic security checks. Therefore, I transitioned to using the Flask framework for the final version of my mock API.

### Python Decorators
I took the time to learn how Python decorators work and how to use them to better understand the construction of a Flask server.

### Deployment on Render.com
I deployed the mock API on Render.com. You can access it via the following URL: [https://mock-api-books-1dn8.onrender.com/](https://mock-api-books-1dn8.onrender.com/).




