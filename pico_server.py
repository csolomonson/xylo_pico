import socket
#import threading

    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = '10.30.21.200'
PORT = 8000

server.bind((SERVER_IP,PORT))
server.listen(0)
print(f'listening on {SERVER_IP}:{PORT}')

client_socket, client_address = server.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')

while True:
        request = client_socket.recv(1024)
        request = request.decode('utf-8')
        print("RECV>> " + request)


    


          
