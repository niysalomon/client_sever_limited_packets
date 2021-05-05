import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1231
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [ help ] to get help\n")
message =''
while True:
    messagez = s.recv(1024)
    messagez = messagez.decode()
    # chunk=[]
    # for word in message:
    #     messagez = chunk.append(word)
    message += messagez
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "help":
        message = "Tho!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())
    # id_rec +=1
