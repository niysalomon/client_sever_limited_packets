#!/usr/bin/env python3
import time, socket, sys
from textwrap import wrap
import arguments
from arguments import *
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 60001
s.bind((host, port))
print(host, "(", ip, ")\n")
name = 'server'
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
    message_recieved = conn.recv(1024)
    message_rec_decoded = message_recieved.decode()
    print(s_name, ":", message_rec_decoded)
    input_message = input(str("Me : "))
    chunk_messages = wrap(input_message, chunks)
    chunk_messages_str= str(chunk_messages)
    print(chunk_messages_str)
    conn.send(chunk_messages_str.encode())
