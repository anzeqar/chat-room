#!/usr/bin/python3

import socket
import threading
from colorama import Fore

name=input('Choose a username: ')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',52525)) 

def receive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='NAME':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:
            print('Connection lost with server')
            client.close()
            break

def write():
    while True:
        text=input('')
        message=Fore.CYAN+f'{name}: '+Fore.WHITE+f'{text}'
        client.send(message.encode('ascii'))


receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()