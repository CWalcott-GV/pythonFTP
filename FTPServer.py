import socket
import os

SERVER_ROOT = "./server_files"

def list_files():
    files = os.listdir(SERVER_ROOT)
    return "\n".join(files)

def retrieve_file(filename):
    try:
        with open(os.path.join(SERVER_ROOT, filename), 'rb') as file:
            return file.read()
    except FileNotFoundError:
        return b"File not found."

def store_file(filename, data):
    with open(os.path.join(SERVER_ROOT, filename), 'wb') as file:
        file.write(data)
    return "File stored successfully."

def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        command = data.split()
        if command[0] == "LIST":
            client_socket.send(list_files().encode())
        elif command[0] == "RETRIEVE":
            filename = command[1]
            client_socket.send(retrieve_file(filename))
        elif command[0] == "STORE":
            filename = command[1]
            data = client_socket.recv(1024)
            response = store_file(filename, data)
            client_socket.send(response.encode())
        elif command[0] == "QUIT":
            break

    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("FTP Server listening on {}:{}".format(host, port))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected to {}".format(addr))
        handle_client_connection(client_socket)

    server_socket.close()

if __name__ == "__main__":
    start_server("127.0.0.1", 8888)
