import socket
def start_client():
    host = '127.0.0.1'  # localhost
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("[CONNECTED] Connected to server.")

    while True:
        # Send message to server
        msg = input("Send Message: ")
        client.send(msg.encode('utf-8'))

        # Receive echoed message from server
        recv_msg = client.recv(1024).decode('utf-8')
        print(f"Server Message Received: {recv_msg}")

    client.close()
    
if __name__ == "__main__":
    start_client()