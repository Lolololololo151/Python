import socket
import threading

class Server:
    def __init__(self):
        self.server_socket = socket.create_server(("localhost", 5959))
        self.server_socket.setblocking(False)
        self.clients = []
        self.accept_thread = threading.Thread(target=self.accept_loop)
        self.receive_thread = threading.Thread(target=self.receive_loop)
        self.accept_thread.start()
        self.receive_thread.start()
        self.accept_thread.join()
        self.receive_thread.join()

    def accept_loop(self):
        while True:
            try:
                self.server_accept = self.server_socket.accept()[0]
                self.server_accept.setblocking(False)
                msg = f"Welcome User{len(self.clients)} on server!\n"
                self.server_accept.send(msg.encode())
                for client in self.clients:
                    msg = f"User{len(self.clients)} joined.\n"
                    client.send(msg.encode())
                self.clients.append(self.server_accept)
            except BlockingIOError:
                pass

    def receive_loop(self):
        while True:
            for i, client in enumerate(self.clients):
                try:
                    data = client.recv(1024)
                    if data == b"":
                        client.close()
                    data = data.decode()
                    for c in self.clients:
                        msg = f"User{i}: {data}\n"
                        c.send(msg.encode())
                except BlockingIOError:
                    pass

try:
    server = Server()
except KeyboardInterrupt:
    exit() 