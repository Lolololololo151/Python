import socket

#server = socket.create_server(("192.168.1.129", 5959))
server = socket.create_server(("localhost", 5959))
client = server.accept()[0]
client.send(b"You're connected!!! Sending viruses right Now!")
# client.send(b"The virus was sent")
while True:
    to_Send = input("(server)> ")
    print("Waiting for answer...")
    print('\x1b[1A\x1b[2K', end="")
    client.send(to_Send.encode("utf-8"))
    data = client.recv(1024)
    print(f"(client): {data.decode()}")
