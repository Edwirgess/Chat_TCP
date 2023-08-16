import socket

import threading


def recibe_msg(client):

    while True:
        msg = client.recv(1024).decode('utf-8')
        
        if msg == 'x':
            break

        else:
            print(msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 3001))
            
    
recibe_thread = threading.Thread(target= recibe_msg, args=(client, ))
recibe_thread.start()



print('Digite "x" para encerrar')

finish = False

while not finish:
    send = input('Message: ')
    client.send(send.encode('utf-8'))
    if send == 'x':
            fin = True
    




