import time, threading # or use threading.Thread().start()
from socket import * # get socket constructor and constants

myHost = 'localhost' # server machine, '' means local host
myPort = 50008 # listen on a non-reserved port number
sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP socket object
sockobj.bind((myHost, myPort)) # bind it to server port number
sockobj.listen(5) # allow up to 5 pending connects

def now():
    return time.ctime(time.time()) # current time on the server

def handleClient(connection): # in spawned thread: reply
    time.sleep(5) # simulate a blocking activity
    while True: # read, write a client socket
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()

def dispatcher(): # listen until process killed
    while True: # wait for next connection,
        connection, address = sockobj.accept() # pass to thread for service
        print('Server connected by', address,' at ' ,now())
        print('at', now())
        t = threading.Thread(target=handleClient, args=(connection,))
        t.start()
        #thread.start_new_thread(, (connection,))

dispatcher()
