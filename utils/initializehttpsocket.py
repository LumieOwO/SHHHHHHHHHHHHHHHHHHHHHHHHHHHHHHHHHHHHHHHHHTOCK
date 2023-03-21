import socket
from threading import Thread

class InitializeHttpSocket:
    def __init__(self, HOST: str, PORT: int,html_file):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        temp = open(html_file)
        self.response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{temp.read()}"
        temp.close()
        print(f"uwuing in http://{HOST}:{PORT}")
        Thread(target=self.listen_to_connection()).start()


    def listen_to_connection(self):
        while True:
            self.socket.listen()
            conn, addr = self.socket.accept()
            with conn:
                #while True:
                #    data = conn.recv(1024)
                #    if not data or data == '' or len(data) == 0: break
                conn.sendall(bytes(self.response,"utf-8"))
                conn.close()
