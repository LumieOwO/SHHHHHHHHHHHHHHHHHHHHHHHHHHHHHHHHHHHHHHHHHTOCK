import socket
from utils.initializehttpsocket import InitializeHttpSocket
from threading import Thread

def NUTS():
    print("nutsocket")

if __name__ == "__main__":    
    webpage = InitializeHttpSocket(HOST="localhost", PORT=80)
    Thread(target=webpage.add_endpoint(endpoint="/uwu",
           html_file="OWO/ilovehate.html", METHOD=["POST","GET"],function_hook=NUTS)).start()
    Thread(target=webpage.add_endpoint(endpoint="/",
            html_file="OWO/test.html",METHOD=["GET"])).start()
    Thread(target=webpage.run()).start()
