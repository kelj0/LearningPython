import socket, select, sys
from client import Client

CONNECTION_LIST = {}
RECV_BUFFER = 4096
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)
CONNECTION_LIST[server_socket]='SERVER'
        
def broadcast(sock,msg,adr):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send("{0}: {1}".format(CONNECTION_LIST[sock],msg.decode()).encode())
                print("{0}[{1}:{2}]: {3}----------".format(CONNECTION_LIST[sock],adr[0],adr[1],msg.decode()))
            except:
                socket.close()
                CONNECTION_LIST.pop(socket,None)

def printActive():
    for socket in CONNECTION_LIST:
        if socket != server_socket:
            print("%s" % socket)


def startServer():
    print("Chat server started on port " + str(PORT))
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:    
            #New connection
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                sockfd.send("Enter username: ".encode())
                user = Client(addr[0],addr[1],str(sockfd.recv(1024).decode())[:-2])
                CONNECTION_LIST[sockfd] = user.getUsername()
                print("[{0}:{1}] {2} connected".format(addr[0],addr[1],user.getUsername()))
            #Some incoming message from a client
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(sock,data,addr)
                except:
                    print("[{0}:{1}] {2} disconnected".format(addr[0],addr[1],user.getUsername()))
                    printActive()
                    sock.close()
                    CONNECTION_LIST.pop(sock,None)
                    continue
