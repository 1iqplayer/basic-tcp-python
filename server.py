import socket

FIRST_MSG_SIZE = 10
BUFFER_SIZE = 16

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))

s.listen(1)

can_go = False # DISCONNECT FLAG
shut_down = False # SHUTDOWN FLAG
while True:
    if shut_down:
        s.close()
        break

    clientsocket, address = s.accept()
    print(f"connected with {address}")

    #DATA RECEIVE LOOP
    msg_len = 0
    full_msg = ''
    first_message = True
    while True: 
        data = clientsocket.recv(BUFFER_SIZE).decode("utf-8")
        #RECEIVE FIRST BUFFER SIZE MESSAGE
        if first_message:
            first_message = False
            msg_len = int(data[:FIRST_MSG_SIZE])
            print(f"message size: {msg_len}")

        full_msg += data
        #IF FULL MESSAGE WAS RECEIVED
        if len(full_msg[FIRST_MSG_SIZE:]) == msg_len:
            print("Message received succesfully!")
            print(f"MESSAGE: {full_msg[FIRST_MSG_SIZE:]}")
            clientsocket.send('OK'.encode("ascii"))
            clientsocket.close()
            #CHECK FOR EXIT COMMAND
            if full_msg[FIRST_MSG_SIZE:] == "SHUTDOWN": shut_down = True
            break

print("server was closed.")