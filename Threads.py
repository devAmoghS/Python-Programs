import os
import threading, time
aList=[]
count = 0
while count<5:
    ipadd=input("Enter the IP address : ")
    aList.append(ipadd)
    count = count+1

def ping(ip):
    print("Starting ping "+ip)
    result = os.popen("ping "+ip).read()
    print(result)

cnt=0
while cnt<len(aList):
    t=threading.Thread(target=ping,args=(aList[cnt],))
    t.start()
    cnt=cnt+1

time.sleep(20)
    
