import socket
import threading


host = '127.0.0.1'
port = 55555

myServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myServer.bind((host, port))
myServer.listen()

#Lists of clients and their alias
clients = []
nicknames = []

#sending Mesgs to all connected clients(broadcasting)

def broadcast(message):
    for client in clients:
            client.send(message)

#Handling client meassages
def handle(client):
      while True:
            try:
                  #Broadcasting messages
                  message = client.recv(1024)
                  broadcast(message)
            except:
                  #Removing and closing clients
                  index = clients.index(client)
                  clients.remove(client)
                  client.close()
                  nickname = nicknames[index]
                  broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                  nicknames.remove(nickname)
                  break
#Receiving / Listening Function
def recieve():
      while True:
           #accept connection
           client, address = myServer.accept()
           print('Succesful Connection with {}'.format(str(address)))

           #Request and store nickname
           client.send('NICK'.encode('ascii'))
           nickname = client.recv(1024).decode('ascii')
           nicknames.append(nickname)
           clients.append(client)

           #Print and Broadcast Nickname
           print("Nickname is {}".format(nickname))
           broadcast(f'{nickname} joined the chat!'.encode('ascii'))
           client.send("Connected to Server".encode('ascii'))

           #Start a new thread for handling client messages
           thread = threading.Thread(target=handle, args=(client,))
           thread.start()


recieve()