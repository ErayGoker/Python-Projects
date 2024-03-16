import socket
import os
import threading
from threading import Thread

lock=threading.Lock()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 81))  # IP adresi ve portu ayarla
server_socket.listen(1)  # Bağlantıları dinle

print("Sunucu başlatıldı. İstemciyi bekliyor...")

# İstemci bağlantısını kabul et
client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

def write():

    while True:

        if os.path.getsize("server.txt")!=0:
            with open("server.txt", "r+") as file:
                data = file.read()
                if data!=None:
                    client_socket.sendall(data.encode())
                    file.truncate(0)





def read():
    # İstemciden veri al
    while True:
        received_data = client_socket.recv(1024).decode()

        # Alınan veriyi ekrana yazdır
        print("Alınan Veri (client):", received_data)









threadWrite = Thread(target=write)
threadRead = Thread(target=read)


threadWrite.start()
threadRead.start()

threadWrite.join()


