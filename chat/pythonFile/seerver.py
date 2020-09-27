from socket import *
import selectors

selector = selectors.DefaultSelector()
URLS = {
    '/': 'HTTP/1.1  200 OK\r\n\r\n<style>div{margin-top:40px;margin-left:30px}</style> <div><a href=/register>register</a> <br> <a href=/login>login</a></div>',
    '/register': 'HTTP/1.1  200 OK\r\n\r\n',
    '/login': 'HTTP/1.1  200 OK\r\n\r\n'
}

def selectReg(obj, num, setData):
    read = selectors.EVENT_READ
    write = selectors.EVENT_WRITE

    if num == 0:
        selector.register(fileobj=obj, events=read, data=setData)
    else:
        selector.register(fileobj=obj, events=write, data=setData)

def sendDataPost():
    pass

def serverStart():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('', 8080))
    sock.listen()

    selectReg(sock, 0, acceptConnection)



def acceptConnection(socket):
    client, addr = socket.accept()

    selectReg(client, 0, getRequest)



def checkRequest(request):
    lst = request.split(' ')
    method = lst[0]
    urlRequest = lst[1]

    if method == 'GET':
        for key in URLS:
            if key == urlRequest:
                print(urlRequest)
                return URLS[key]

        print(urlRequest)
        return 'HTTP/1.1 404 NOT FOUND\r\n\r\n <h1>ERROR 404 <BR> NOT FOUND</h1>'
    elif method == 'POST':

        pass





def getRequest(client):
    request = client.recv(1024)
    if request:
        selector.unregister(client)
        print('yes connect')

        response = checkRequest(request.decode())
        if response:
            client.send(response.encode())

    client.close()




def eventLoop():
    serverStart()
    while True:
        events = selector.select()

        for key, _ in events:
            callBack = key.data
            callBack(key.fileobj)

if __name__ == '__main__':
    eventLoop()




