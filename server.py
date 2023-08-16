import socket

import threading


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 3001))

servidor.listen()

list_clients = []

def conection_client (client, list_clients):

    while True:
        ms = cliente.recv(1024).decode('utf-8')        
        if ms == 'x':
            break
        else:
            print(ms)
        for connect in list_clients:
            if connect != client:
                connect.send(ms.encode('utf-8'))
                
    client.close()


def send_server ():

    while True:
        send = input('Message: ')
        for connect in list_clients:
            connect.send(send.encode('utf-8'))
           

server_thread = threading.Thread(target=send_server)
server_thread.start()



while True:
    cliente, end = servidor.accept()
    list_clients.append(cliente)
    cliente_thread = threading.Thread(target=conection_client, args=(cliente, list_clients))
    cliente_thread.start()




# cliente.close()
# servidor.close()