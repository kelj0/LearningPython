import socket, select, sys
from multiprocessing import Process
from client import Client

CONNECTION_LIST = {}
RECV_BUFFER = 4096
CHAT_PORT = 5000
ADMIN_PORT = 9050


def broadcast(sock,msg,adr,chatSocket):
    for socket in CONNECTION_LIST:
        if socket != chatSocket and socket != sock:
            try:
                socket.send("{0}: {1}".format(CONNECTION_LIST[socket],msg.decode()).encode())
                print("{0}[{1}:{2}]: {3}----------".format(CONNECTION_LIST[socket],adr[0],adr[1],msg.decode()))
            except:
                socket.close()
                CONNECTION_LIST.pop(socket,None)

def printActive(server_socket):
    for socket in CONNECTION_LIST:
        if socket != server_socket:
            print("%s" % socket)

def listen(ip,port,max_connections):
    print("Starting listener on port %s" % str(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(max_connections)
    print("Listening on port %s" % str(port))
    return s

def startChatRoom(ip,port):
    print("Starting chat room on port %s..." % str(port))
    s = listen(ip,port,10)
    CONNECTION_LIST[s] = 'chatSocket'
    while 1:
        read_sockets = select.select(CONNECTION_LIST,[],[])[0]
        for sock in read_sockets:
            if sock == s:
                sockfd, addr = s.accept()
                sockfd.send("Enter username: ".encode())
                user = Client(addr[0],addr[1],str(sockfd.recv(1024).decode())[:-2])
                CONNECTION_LIST[sockfd] = user.getUsername()
                print("[{0}:{1}] {2} connected".format(addr[0],addr[1],user.getUsername()))
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(sock,data,addr,s)
                except:
                    print("[{0}:{1}] {2} disconnected".format(addr[0],addr[1],user.getUsername()))
                    printActive()
                    sock.close()
                    CONNECTION_LIST.pop(sock,None)
                    continue

def startAdminPanel(ip,port):
    print("Starting admin pannel on port %s" % str(port))
    s = listen(ip,port,1)
    print("Waiting for admin connection")
    logged_in = False
    connections = [s]
    while 1:
        r = select.select(connections,[],[])[0]
        for sock in r:
            if sock == s:
                if not logged_in:
                    sock, addr = s.accept()
                    connections.append(sock)
                    sock.send("Username: ".encode())
                    username = str(sock.recv(RECV_BUFFER).decode())
                    print("Admin connected %s" % username)
                    logged_in = True
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        sock.send(("Got your message: %s" % data.decode()).encode())
                except:
                    print("Admin disconnected")
                    logged_in = False
                    sock.close()
                    continue

def startServer():
    chatRoomProcess = Process(target=startChatRoom, args=('0.0.0.0',CHAT_PORT,))
    adminPanelProcess = Process(target=startAdminPanel, args=('0.0.0.0',ADMIN_PORT,))
    chatRoomProcess.start()
    adminPanelProcess.start()
