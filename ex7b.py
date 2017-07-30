import sys
from socket import * # portable socket interface plus constants
serverHost = "localhost" # server name, or: 'starship.python.net'
serverPort = 50008 # non-reserved port used by the server

message = ['Hello network world'.encode()] # default text to send to server

sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort)) # connect to server machine + port

for line in message:
    sockobj.send(line) # send line to server over socket
    data = sockobj.recv(1024) # receive line from server: up to 1k
    print('Client received:', data) # bytes are quoted, was `x`, repr(x)

sockobj.close() # close socket to send eof to server
