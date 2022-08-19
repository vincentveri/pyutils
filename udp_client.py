import socket


if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"AAABBBCCC", (target_host, target_port))

    try:
        data, addr = client.recvfrom(4096)
        print(data)
    except ConnectionResetError as e:
        print(e)

    print("Programma terminato.")