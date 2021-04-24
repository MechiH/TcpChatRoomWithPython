import threading
import socket

nickname=input('choose a nickanme: ')

client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))


def receive():
    while True:
        try: # receive messages fromserever we consider the server as a client
            message=client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break
def write():
    while True:
        message=f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# create a recevie thread and a send thread
receiveThread= threading.Thread(target=receive)
receiveThread.start()

sendThread= threading.Thread(target=write)
sendThread.start()