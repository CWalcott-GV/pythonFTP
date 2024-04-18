import socket
import os

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", port))
    server_socket.listen(1)
    print("FTP server started.")
    return server_socket

def handle_client(client_socket):
    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break
        if command.upper() == "QUIT":
            break
        elif command.upper() == "LIST":
            files_list = "\n".join(os.listdir())
            client_socket.send(files_list.encode())
        elif command.upper().startswith("RETRIEVE"):
            filename = command.split()[1]
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    file_data = file.read()
                    client_socket.send(file_data)
            else:
                client_socket.send("File not found.".encode())
        elif command.upper().startswith("STORE"):
            filename 