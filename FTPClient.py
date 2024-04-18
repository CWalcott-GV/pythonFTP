import socket
import os

def connect_server(server_address, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    return client_socket

def send_command(client_socket, command):
    client_socket.send(command.encode())

def receive_response(client_socket):
    response = client_socket.recv(1024).decode()
    return response

def list_files(client_socket):
    send_command(client_socket, "LIST")
    files_list = receive_response(client_socket)
    print("Files at server:", files_list)

def retrieve_file(client_socket, filename):
    send_command(client_socket, f"RETRIEVE {filename}")
    file_data = client_socket.recv(1024)
    with open(filename, "wb") as file:
        file.write(file_data)
    print(f"File {filename} retrieved successfully.")

def store_file(client_socket, filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return
    send_command(client_socket, f"STORE {filename}")
    with open(filename, "rb") as file:
        file_data = file.read()
        client_socket.send(file_data)
    print(f"File {filename} stored successfully.")

def disconnect(client_socket):
    send_command(client_socket, "QUIT")
    client_socket.close()

def main():
    server_address = input("Enter server address: ")
    server_port = int(input("Enter server port: "))
    client_socket = connect_server(server_address, server_port)
    while True:
        command = input("Enter command (LIST, RETRIEVE <filename>, STORE <filename>, QUIT): ")
        if command.upper() == "LIST":
            list_files(client_socket)
        elif command.upper().startswith("RETRIEVE"):
            filename = command.split()[1]
            retrieve_file(client_socket, filename)
        elif command.upper().startswith("STORE"):
            filename = command.split()[1]
            store_file(client_socket, filename)
        elif command.upper() == "QUIT":
            disconnect(client_socket)
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
