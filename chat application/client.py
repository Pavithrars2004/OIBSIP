import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    host = '127.0.0.1'  # Localhost
    port = 12345
    client_socket.connect((host, port))
    
    while True:
        # Send a message to the server
        message = input("You: ")
        client_socket.send(message.encode())
        
        # Receive the server's response
        reply = client_socket.recv(1024).decode()
        if not reply:
            break
        print(f"Server: {reply}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
