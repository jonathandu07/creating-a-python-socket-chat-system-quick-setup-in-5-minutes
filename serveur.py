import socket
import threading

def start_server():
    host = '127.0.0.1'  # localhost
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()
        
        
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        # Receive message from client
        msg = client_socket.recv(1024).decode('utf-8')
        if not msg:
            break
        
        print(f"Client Message Received: {msg}")

        msg = input("Send Message: ")

        # Echo message back to client
        client_socket.send(msg.encode('utf-8'))

    print(f"[DISCONNECTED] {addr}")
    client_socket.close()
    
if __name__ == "__main__":
    start_server()