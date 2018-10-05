import socket
from _thread import start_new_thread
import time
import os,sys

HOST = ''
PORT = 5000

def clientThread(conn,addr):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            conn.send(str.encode('HTTP/1.0 200 OK\n'))
            conn.send(str.encode('Content-Type: text/html\n\n'))
            conn.send(str.encode(''.join(open('hello.html','r').readlines())))
        except OSError:
            continue
        print("Response sent to client")
        conn.close()
        


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    print("Socket created")
    try:
        s.bind((HOST,PORT))
    except socket.error as e:
        print(str(e))
    print("Socket bind complete")

    
    s.listen(5)
    print("Socket now listening")

    while True:
        conn, addr = s.accept()
        print("Connected to {0}:{1}".format(addr[0],addr[1]))
        start_new_thread(clientThread,(conn,addr,))
    s.close()



if __name__ == "__main__":
    main()