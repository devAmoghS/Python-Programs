import os
import threading,time
l=[]
i=0
while i<3:
    x=input("enter the ip address=")
    l.append(x)
    i=i+1

def ping(ip):
     os.system("ping "+ip)
    

i=0
while i<len(l):
  #  if threading.activecount()<len(l):
        t=threading.Thread(target=ping,args=(l[i],))
        t.start()
        i=i+1

time.sleep(20)

