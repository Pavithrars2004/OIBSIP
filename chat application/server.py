import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name and bind to a port
    host = '127.0.0.1'  # Localhost
    port = 12345
    server_socket.bind((host, port))
    
    # Listen for incoming connections (1 connection at a time)
    server_socket.listen(1)
    print(f"Server started at {host} on port {port}. Waiting for a connection...")
    
    # Accept the connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")
    
    while True:
        # Receive data from the client
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Client: {message}")
        
        # Send a response back to the client
        reply = input("You: ")
        client_socket.send(reply.encode())
    
    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
