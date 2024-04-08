import socket

def connect_to_server(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    return client_socket

def send_command(client_socket, command):
    client_socket.send(command.encode())
    return client_socket.recv(1024).decode()

def main():
    server_host = input("Enter server hostname/IP address: ")
    server_port = int(input("Enter server port number: "))

    client_socket = connect_to_server(server_host, server_port)

    while True:
        command = input("FTP> ").strip()
        if command.startswith("CONNECT"):
            _, host, port = command.split()
            client_socket = connect_to_server(host, int(port))
        else:
            response = send_command(client_socket, command)
            print(response)

        if command == "QUIT":
            break

    client_socket.close()

if __name__ == "__main__":
    main()
