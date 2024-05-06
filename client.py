import socket
import threading

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)  # Receive data from client
            if not data:
                break
            print(f"Received from {addr}: {data.decode()}")
            conn.sendall(data)  # Echo back the received data
    finally:
        conn.close()

def tcp_server():
    host = '127.0.0.1'
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"TCP Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

# Uncomment the following line to run the TCP server
# tcp_server()
