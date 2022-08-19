import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"dir")

# receive some data
response = client.recv(512)

print(response)