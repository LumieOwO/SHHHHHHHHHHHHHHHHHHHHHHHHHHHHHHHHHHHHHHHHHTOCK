import socket
from threading import Thread


class InitializeHttpSocket:
    def __init__(self,
                 HOST: str,
                 PORT: int,
                 ) -> None:
        self.__HOST:str = HOST
        self.__PORT:str = PORT
        self.__endpoints:dict = {}

    def add_endpoint(self, endpoint: str, html_file: str, METHOD=["GET"]) -> None:
        self.__endpoints[endpoint] = [html_file, METHOD]
        return None

    def run(self) -> None:
        self.__socket:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind((self.__HOST, self.__PORT))
        print(f"uwuing in http://{self.__HOST}:{self.__PORT}")
        Thread(target=self.__listen_to_connection()).start()
        return None

    def __handle_request(self, req: str) -> str:
        __parsed_req:str = req.split()
        for endpoint in self.__endpoints:
            if endpoint == __parsed_req[1] and __parsed_req[0] in self.__endpoints[endpoint][1]:
                __html_file:str = self.__endpoints[endpoint][0]
                with open(__html_file) as htmlf:
                    __html_file:str = htmlf.read()
                __response:str = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{__html_file}"
                return __response
        __response:str = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n404 Not Found"
        return __response

    def __handle_connection(self, conn:socket.socket) -> None:
        with conn:
            request = conn.recv(1048576)
            data:str = self.__handle_request(request.decode())
            conn.sendall(data.encode('utf-8'))
            conn.close()
        return None

    def __listen_to_connection(self) -> None:
        while True:
            self.__socket.listen()
            conn,addr = self.__socket.accept()
            Thread(target=self.__handle_connection, args=[conn]).start()
