import SocketServer,socket

ip="127.0.0.1"
port=9999

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message))
        response = str(sock.recv(1024))
        print("Received: {}".format(response))
    finally:
        sock.close()

client(ip,port,"[[600,'abc','c',5],1]")
'''


while 1:
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    sock.connect((ip, port))
    message = raw_input("press : ")
    if message=="":
	    sock.close()
    sock.sendall(bytes(message))
    response = str(sock.recv(1024))
    print("Received: {}".format(response))
    sock.close()

'''
	
'''try:
    sock.sendall(bytes(message))
    response = str(sock.recv(1024))
    print("Received: {}".format(response))'''
