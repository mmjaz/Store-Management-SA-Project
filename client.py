import SocketServer,socket,ast

#ip="127.0.0.1"
#port=9999
#setIP("127.0.0.1",9999)
class Client():
    def __init__(self):
        self.ip="127.0.0.1"
        self.port=9999
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
        if self.res[0]=="[":
            return ast.literal_eval(self.res)
        else:
            return self.res
        
y=Client()
y.send([[""]])

print type(y.get()[0])
print y.get()
