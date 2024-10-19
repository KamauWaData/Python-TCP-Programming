import socket
import threading

#Choosing Nickname
nickname = input("Choose your nickname: ")

#Connecting to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

#Listening and sending nickname to server
def recieve():
    while True:
        try:
            # Receive Msgs from server
            # When 'NICK' send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            #close conection when error
            print("An error occured!")
            client.close()
            break

#Send msgs to the server
def write():
    while True:
        # Sending messages to server
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))


#Starting threads
recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()