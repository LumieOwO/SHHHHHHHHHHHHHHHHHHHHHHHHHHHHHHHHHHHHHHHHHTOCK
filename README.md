The HTTP Server module provides a basic HTTP server that listens on a specified host and port and handles GET and POST requests to different endpoints.

Usage:
To use this module, import it into your script and create an instance of the InitializeHttpSocket class with the desired host and port. You can then use the add_endpoint method to add endpoints to the server, specifying the URL path, HTML file, and HTTP method that the server will handle.

You can also add a function hook to an endpoint to execute custom code when the endpoint is requested. The function hook should be a callable that takes no arguments.

Example:
```python
import socket
from threading import Thread
from http_server import InitializeHttpSocket

def custom_function():
    print("Custom function called")

if __name__ == "__main__":
    # Create HTTP server instance
    webpage = InitializeHttpSocket(HOST="localhost", PORT=80)

    # Add endpoints to the server
    webpage.add_endpoint(endpoint="/", html_file="index.html", METHOD=["GET"])
    webpage.add_endpoint(endpoint="/submit", html_file="submit.html", METHOD=["POST"], function_hook=custom_function)

    # Start the server
    webpage.run()
```

This will start the HTTP server on localhost:80 and handle requests to the "/submit" endpoint with the custom function custom_function.

Requirements:
This module requires Python 3.7 or higher.
