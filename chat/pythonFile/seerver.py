import getpage
import selectors
from socket import *

selector = selectors.DefaultSelector()

lst = getpage.return_page()
print(lst)
URLS = {
    '/': f'HTTP/1.1  200 OK\r\n\r\n',
    '/register': 'HTTP/1.1  200 OK\r\n\r\n',
    '/login': 'HTTP/1.1  200 OK\r\n\r\n'
}



def select_reg(obj, num, setData):
    read = selectors.EVENT_READ
    write = selectors.EVENT_WRITE

    if num == 0:
        selector.register(fileobj=obj, events=read, data=setData)
    else:
        selector.register(fileobj=obj, events=write, data=setData)



def send_data_post(data):
    sock_data_send = socket(AF_INET, SOCK_STREAM)
    sock_data_send.connect('', 8880)
    sock_data_send.send(data)
    response_service = sock_data_send.recv(1024)
    if response_service:
        return response_service
    return 'error'



def server_start():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('', 8080))
    sock.listen()

    select_reg(sock, 0, accept_connection)



def accept_connection(socket):
    client, addr = socket.accept()

    select_reg(client, 0, get_request)



def check_request(request):
    lst = request.split(' ')
    method = lst[0]
    url_request = lst[1]

    if method == 'GET':
        for key in URLS:
            if key == url_request:
                print(url_request)
                return URLS[key]

        print(url_request)
        return 'HTTP/1.1 404 NOT FOUND\r\n\r\n <h1>ERROR 404 <BR> NOT FOUND</h1>'
    elif method == 'POST':
        return 'Error'



def get_request(client):
    request = client.recv(1024)
    if request:
        selector.unregister(client)
        print('yes connect')

        response = check_request(request.decode())
        if response:
            client.send(response.encode())

    client.close()



def event_loop():
    server_start()
    while True:
        events = selector.select()

        for key, _ in events:
            callBack = key.data
            callBack(key.fileobj)

if __name__ == '__main__':
    event_loop()




