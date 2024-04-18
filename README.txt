FTP Client and Server

Description
This project includes two Python scripts: `ftp_client.py` for the FTP client and `ftp_server.py` for the FTP server. 
The client allows users to connect to a server, list files, retrieve files, upload files, and terminate the connection. 
The server listens for client connections and handles file transfers.

How to Run
1. Ensure Python 3 is installed.
2. Download or clone the project.
3. Open a terminal/command prompt in the project directory.

FTP Client
- Run:

  python FTPClient.py

- Follow on-screen instructions.

 FTP Server
- Run:

  python ftp_server.py

- The server listens on localhost:2121 by default.

 Usage Notes
- Start the server before connecting with the client.
- Client commands: `LIST`, `RETRIEVE <filename>`, `STORE <filename>`, `QUIT`.
- Replace `<filename>` with the actual file name.

