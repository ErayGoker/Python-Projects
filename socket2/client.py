import socket
import os
import threading
from threading import Thread


lock=threading.Lock()

server_address = ('localhost', 81)

        # Soket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


     # Sunucuya bağlan
client_socket.connect(server_address)

def write():
    while True:
        if os.path.getsize("client.txt")!=0:
            with open("client.txt", "r+") as file:
                data = file.read()
                if data!=None:
                    client_socket.sendall(data.encode())
                    file.truncate(0)


def read():
    while True:

        # Sunucudan veri al
        received_data = client_socket.recv(1024).decode()

        # Alınan veriyi ekrana yazdır
        print("Alınan Veri (server):", received_data)








threadWrite = Thread(target=write)
threadRead = Thread(target=read)


threadWrite.start()
threadRead.start()
threadWrite.join()
threadRead.join()
