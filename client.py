#!/usr/bin/env python3
import time, socket, sys
import arguments
from arguments import *

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, "(", ip, ")\n")
host = '127.0.1.1'
name = 'Client'
port = 60001
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [ help ] to get help\n")
initial_message =''
while True:
    input_message = input(str("Me : "))
    s.send(input_message.encode())
    message_received = s.recv(1024)
    message_received_decoded = message_received.decode()
    # replaced_messages=''
    # for message in message_received_decoded:
    #     initial_message += message
    # message_striped=message_received_decoded.strip().replace(',','')
    replaced_message=message_received_decoded.replace("'",'')
    replaced_messages=replaced_message.replace("[", '')
    replaced_messages=replaced_messages.replace(', ','')
    print(s_name, ":", replaced_messages.replace("]",''))

