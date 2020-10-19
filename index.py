import socket
import sys
import time
s=socket.socket()
host=input(str("Please enter host name:"))
port=1234
s.connect((host,port))
print("Connected to server")
while 1:
     incoming_message=s.recv(1024)
     incoming_message=incoming_message.decode()
     print("Server:>>",incoming_message)
     message=input(str("Server:>>"))
     message=message.encode()
     s.send(message)
