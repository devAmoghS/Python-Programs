from socket import *

host='localhost'
port=50007
s = socket(AF_INET,SOCK_STREAM)

s.bind( ( host, port ) )

s.listen(5)
while True:
    conn,addr = s.accept()
    print('Got connection from ',addr,conn)
    conn.send(b'Thank you for connecting...')
    conn.close()
