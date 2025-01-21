import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = socket.gethostname()
    print(host)
    port = 12345
    
    # Bind to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    
    print("Server listening on port", port)
    
    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print("Got a connection from", addr)
        
        # Receive message from the client
        message = client_socket.recv(1024).decode('utf-8')
        print("Message from client:", message)
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()