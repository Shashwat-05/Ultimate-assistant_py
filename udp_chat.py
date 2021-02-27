import socket
import threading

#s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(("192.168.29.40",1332))#receiver address

def receiver():
    global s,myip,myport
    s.bind((myip,int(myport)))#receiver address
    Ronline= True
    while Ronline:
        msg_rcv = s.recvfrom(1024)
        print("\t\t\t\t\t\t\t"+msg_rcv[1][0] + " sent : " + msg_rcv[0].decode())
        if msg_rcv[0].decode() == 'bye':
            Ronline = False
    print(msg_rcv[1][0] +" left the chat ")


def sender():
    Sonline=True
    global s,rip,rport
    while Sonline:        
        msg_snt = input('>')
        s.sendto(msg_snt.encode(),(rip,int(rport)))
        
        if msg_snt=='bye':
            confirm=input('close the app? :')
            if confirm=='yes':
                print('you left the chat\n------x------')
                Sonline=False


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

myip,myport=input("enter the IP,port for socket :").split(",")
rip,rport=input("enter the IP,port of receiver :").split(",")

p1=threading.Thread(target=receiver)
p2=threading.Thread(target=sender)

p1.start()
p2.start()
        
