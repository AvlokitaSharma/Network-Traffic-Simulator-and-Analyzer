import socket

def udp_server():
    host = '127.0.0.1'
    port = 5001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
        if len(data) > 1024:
            print(f"Data exceeds buffer size from {addr}, potential buffer overflow attack.")
            continue
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)

# Uncomment the following line to run the UDP server
# udp_server()
