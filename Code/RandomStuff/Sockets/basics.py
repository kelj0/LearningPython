import socket
from _thread import *

HOST = ''
PORT = 5000

def clientThread(conn):
    conn.send(str.encode("Welcome to the server. Type something and hit enter\n"))
    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        start_new_thread(clientThread,(conn,))
    s.close()



if __name__ == "__main__":
    main()