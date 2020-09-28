from socket import *
import selectors

def socketRegister():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('', 8880))
    sock.listen()

def getConnect(sock):
    server, addr = sock.accept()

def getData(server):
    dataPost = server.recv(1024)
