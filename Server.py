import socket
import threading
import SocketServer
import ast

import dbtest
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        data = str(self.request.recv(1024))

        cur_thread = threading.current_thread()
        response = bytes(data)
        b=ast.literal_eval(data)
        print b

        if b[1]=='newEmployeeSQL':
            a=dbtest.insertIntoEmployee(b[0])
            response = bytes(a)
            print response
        elif b[1]=='modifyEmployeeSQL':
            dbtest.updateEmployee(b[0])
        elif b[1]=='removeEmployeeSQL':
            dbtest.deleteEmployee(b[0])

        elif b[1]=='searchAllEmployeeSQL':
            m=dbtest.searchAllEmployee()
            response = (bytes(m))
        elif b[1]=='searchByFirst NameEmployeeSQL':
            o=dbtest.searchByNameEmployee(b[0])
            response = bytes(o)
        elif b[1]=='searchByLast NameEmployeeSQL':
            s=dbtest.searchByLNameEmployee(b[0])
            response = bytes(s)


        elif b[1]=='newKalaSQL':
            dbtest.insertIntoKala(b[0])
        elif b[1]=='modifyKalaSQL':
            dbtest.updateKala(b[0])
        elif b[1]=='removeKalaSQL':
            dbtest.deleteKala(b[0])

        elif b[1]=='searchAllItemSQL':
            n=dbtest.searchKala()
            response = bytes(n)
        elif b[1]=='searchByNameItemSQL':
            t=dbtest.searchByNameKala(b[0])
            response = bytes(t)
        elif b[1]=='searchByNameItemSQL':
            t=dbtest.searchByNameKala(b[0])
            response = bytes(t)
        elif b[1]=='searchByCategoryItemSQL':
            t=dbtest.searchByCategoryKala(b[0])
            response = bytes(t)
        elif b[1]=='searchByNumberItemSQL':
            t=dbtest.searchByNumberKala()
            response = bytes(t)


        elif b[1]=='newProducerSQL':
            dbtest.insertIntoProducer(b[0])
        elif b[1]=='modifyProducerSQL':
            dbtest.updateProducer(b[0])
        elif b[1]=='removeProducerSQL':
            dbtest.deleteProducer(b[0])

        elif b[1]=='searchAllProducerSQL':
            w=dbtest.searchProducer()
            response = bytes(w)
        elif b[1]=='searchByNameProducerSQL':
            q=dbtest.searchByNameProducer(b[0])
            response = bytes(q)
        elif b[1]=='searchByCodeProducerSQL':
            q=dbtest.searchByCodeProducer(b[0])
            response = bytes(q)


        elif b[1]=='newOrderSQL':
            dbtest.insertIntoOrder(b[0])
        elif b[1]=='modifyOrderSQL':
            dbtest.updateOrder(b[0])
        elif b[1]=='removeOrderSQL':
            dbtest.deleteOrder(b[0])

        elif b[1]=='searchAllOrderSQL':
            m=dbtest.searchOrder()
            response = (bytes(m))
        elif b[1]=='searchByNameOrderSQL':
            o=dbtest.searchByNameOrder(b[0])
            response = bytes(o)
        elif b[1]=='searchByCodeOrderSQL':
            s=dbtest.searchByCodeOrder(b[0])
            response = bytes(s)



        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
'''
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message))
        response = str(sock.recv(1024))
        print("Received: {}".format(response))
    finally:
        sock.close()'''

if __name__ == "__main__":
    # port 0 means to select an arbitrary unused port
    HOST, PORT = "", 9999

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    print ip ,port

    # start a thread with the server. 
    # the thread will then start one more thread for each request.
    server_thread = threading.Thread(target=server.serve_forever)

    # exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    server.serve_forever()
    #server.shutdown()
    

   
