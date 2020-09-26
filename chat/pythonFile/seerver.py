from socket import *
import selectors

selector = selectors.DefaultSelector()


def selectReg(obj, num, setData):
    read = selectors.EVENT_READ
    write = selectors.EVENT_WRITE

    if num == 0:
        selector.register(fileobj=obj, events=read, data=setData)
    else:
        selector.register(fileobj=obj, events=write, data=setData)



def serverStart():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('', 8080))
    sock.listen()

    selectReg(sock, 0, acceptConnection)


def acceptConnection(socket):
    client, addr = socket.accept()

    selectReg(client, 0, getRequest)



def getRequest(client):
    request = client.recv(1024)
    if request:
        selector.unregister(client)
        print('yes connect')
    client.close()

def setResponse(clien):
    pass

def eventLoop():
    serverStart()
    while True:
        events = selector.select()

        for key, _ in events:
            callBack = key.data
            callBack(key.fileobj)

if __name__ == '__main__':
    eventLoop()




