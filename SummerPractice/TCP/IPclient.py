import socket
from TCP import IPserver

s= socket.socket()

s.connect('localhost', 4000)

message = s.recv(1024)

while message:
    print(" gotcha!",message.decode(1024))
    message = s.recv(1024)

s.close()
