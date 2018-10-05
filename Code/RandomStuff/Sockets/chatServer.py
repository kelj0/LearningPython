import socket, select

CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(10)
CONNECTION_LIST.append(server_socket)
        
def broadcast(sock,msg):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(msg)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)

def printActive():
    for socket in CONNECTION_LIST:
        if socket != server_socket:
            print("%s" % socket)

def main():
    print("Chat server started on port " + str(PORT))
    while 1:
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
        for sock in read_sockets:    
            #New connection
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print("Client (%s:%s) connected" % addr)
            #Some incoming message from a client
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(sock,"[{0}:{1}]: {2}\n"\
                        .format(addr[0],addr[1],data.decode()).encode())
                        print("[{0}:{1}]: {2}".format(addr[0],addr[1],data.decode()))
                except:
                    sock.sendall(("Client [%s:%s] disconnected" % addr).encode())
                    print("Client [%s:%s] disconnected" % addr)
                    printActive()
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

if __name__ == '__main__':
    main()