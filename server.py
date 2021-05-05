#!/usr/bin/env python3
import time, socket, sys
from textwrap import wrap

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1231
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
chunks = input("Enter limit size: ")
chunks=int(chunks)
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [ help ] to get help!\n")
conn.send(name.encode())

while True:
    messag = input(str("Me : "))
    messages = wrap(messag, chunks)
    message= str(messages)


    print(message)

    if message == "help":
        message = "this is help guys"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    mess = conn.recv(1024)
    mess = mess.decode()
    message = wrap(mess, chunks)
    message= str(messages)
    print(s_name, ":", message)