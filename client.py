import socket

FIRST_MSG_SIZE = 10
END_SOCKET = 192.168.1.20, 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(END_SOCKET)

msg = "SHUTDOWN"
msg = f'{len(msg):<10}' + msg

print(f"sending a message...")
s.send(msg.encode("utf-8"))
status = s.recv(2).decode("ascii")

if status == "OK": print("message sended succesfuly!")
else : print("failed to send message!")
