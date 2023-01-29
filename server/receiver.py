import socket

# Create a socket object
# serversocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sendout(msg):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('10.0.2.2', 8000))
    # serversocket.listen(5)
    serversocket.send("nihao".encode())



while True:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a specific address and port
    serversocket.bind(('10.130.230.92', 22341))

    # Listen for incoming connections
    serversocket.listen(5)
    # Establish a connection with a client

    # Receive data from the client
    (clientsocket, address) = serversocket.accept()
    print(f'Connection from {address} has been established.')
    data = clientsocket.recv(1024)
    print(data.decode())
    serversocket.close()
    clientsocket.close()
    break

# sendout("hah")


    


