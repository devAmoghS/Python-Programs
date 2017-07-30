from socket import *

host='localhost'
port=50007
s = socket(AF_INET,SOCK_STREAM)

s.connect((host,port))

print(s.recv(1024))
input()
s.close()
