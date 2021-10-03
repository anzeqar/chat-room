#!/usr/bin/python3

import socket
import threading

host='127.0.0.1'
port=52521

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients=[]
names=[]


def receive():
    while True:
        client,address=server.accept()
        print(f'Connected with {str(address)}'.encode('ascii'))
        client.send('NAME'.encode('ascii'))
        name=client.recv(1024).decode('ascii')
        names.append(name)
        print(f'{name} has joined the chat'.encode('ascii'))

        broadcast(f'{name} has joined the chat room'.encode('ascii'))
        clients.append(client)

        client.send('You have joined the chat room'.encode('ascii'))

        thread=threading.Thread(target=(handle), args=(client,))
        thread.start()



def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            broadcast(f'{name} has left the chat'.encode('ascii'))
            names.remove(name)
            break


def broadcast(message):
    for client in clients:
        client.send(message)



print('Server Started')
receive()



