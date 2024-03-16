import socket
import os
import threading
from threading import Thread


lock = threading.Lock()
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 80))  # IP adresi ve portu ayarla
    server_socket.listen(1)  # Bağlantıları dinle

    print("Sunucu başlatıldı. İstemciyi bekliyor...")

    client_socket, client_address = server_socket.accept()
    print(f"{client_address} bağlandı.")

    try:
        while True:
            with open("server.txt", "r+") as file:
                data = file.read()
                if data==None:
                    lock.acquire()
            client_socket.sendall(data.encode())

            received_data = client_socket.recv(1024).decode()

            print("Alınan Veri (client):", received_data)



            while os.path.getsize("server.txt") != 0:
                file.truncate(0)
    except ConnectionResetError:
        print("İstemci bağlantısı koptu. Tekrar bekleniyor...")
        client_socket, client_address = server_socket.accept()
        print(f"{client_address} bağlandı.")

    # Bağlantıyı kapat
    client_socket.close()

if __name__ == "__main__":
    main()
