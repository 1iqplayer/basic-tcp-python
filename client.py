import socket

FIRST_MSG_SIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3234))

whole = ''
new_msg = True
msg_size = 0
while True:
    msg = s.recv(16)
    if new_msg:
        new_msg = False
        print(f"new message size: {msg[:FIRST_MSG_SIZE]}")
        msg_size = int(msg[:FIRST_MSG_SIZE])
    
    whole += msg.decode("utf-8")

    if len(whole) - FIRST_MSG_SIZE == msg_size:
        print("full mess recvd")
        print(whole[FIRST_MSG_SIZE:])
        s.send("OK".encode("utf-8"))

