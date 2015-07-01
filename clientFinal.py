import SocketServer,socket

#ip="127.0.0.1"
#port=9999
#setIp("127.0.0.1",9999)

class Client():

    def __init__(self):
        self.ip=""
        self.port=0
        self.res=""
        
    def setIP(self,ip,port):
        self.ip=ip
        self.port=port
    
    def send(self,message):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        self.sock.sendall(bytes(message))
        self.res = str(self.sock.recv(1024))
        self.sock.close()
        
    def get(self):
        return self.res
        
