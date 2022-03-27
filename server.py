import socket

FIRST_MSG_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3234))

s.listen(3)

can_go = False
while True:
    clientsocket, address = s.accept()
    print(f"connected with {address}")

    msg = "hi my name is slim shady, im a alcoholic and i like to beat my mom"
    msg = (f'{len(msg):<{FIRST_MSG_SIZE}}' + msg).encode("utf-8")
    clientsocket.send(msg)
    
    if clientsocket.recv(2).decode("utf-8") == "OK":
        print("Message transmitted succesfully!")
        clientsocket.close()
        can_go = True
    
    if can_go: break
