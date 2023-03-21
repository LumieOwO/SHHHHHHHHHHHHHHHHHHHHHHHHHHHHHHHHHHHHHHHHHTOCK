import socket
from utils.initializehttpsocket import InitializeHttpSocket

if __name__ == "__main__":
    InitializeHttpSocket(HOST="localhost",PORT=6942,html_file="test.html")