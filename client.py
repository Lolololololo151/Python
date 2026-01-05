import socket

client = socket.create_connection(("192.168.0.169", 5959))
#client = socket.create_connection(("localhost", 5959))
data = client.recv(1024)
print(f"(server): {data.decode()}")
# data = client.recv(1024)
# print(f"(server): {data.decode()}")
while True:
    print("Waiting for answer...")
    data = client.recv(1024)
    print('\x1b[1A\x1b[2K', end="")
    print(f"(server): {data.decode()}")
    
    to_Send = input("(you)> ")
    
    client.send(to_Send.encode("utf-8"))
    