import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class chatGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.chat_area = scrolledtext.ScrolledText()
        self.chat_area.configure(state="disabled")
        self.chat_area.pack(fill="both")

        self.message_input = scrolledtext.ScrolledText(self.root, height=2)
        self.message_input.pack(fill="x")

        self.send_button = tk.Button(self.root, text="Send", command=self.send)
        self.send_button.pack(fill="x")
        self.root.protocol("VM_DELETE_WINDOW", self.on_closing)
        #self.client_socket = socket.create_connection(("localhost", 5959))
        self.client_socket = socket.create_connection(("192.168.0.182", 5959))
        self.client_socket.setblocking(False)
        self.receive_thread = threading.Thread(target=self.receive_loop)
        self.receive_thread.start()
        self.root.mainloop()
        self.receive_thread.join()
    
    def on_closing(self):
        print("Final massage")
        self.client_socket.close()
        self.root.destroy

    def send(self):
        text = self.message_input.get("1.0", "end")
        text = text.strip()
        self.message_input.delete("1.0", "end")
        if text:
            print(text)
            self.client_socket.send(text.encode())

    def receive_loop(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if data == b"":
                    break
                data = data.decode()
                self.chat_area.configure(state="normal")
                self.chat_area.insert("end", data)
                self.chat_area.configure(state="disabled")
            except BlockingIOError:
                pass
            except OSError:
                pass

ChatGUIW = chatGUI()
