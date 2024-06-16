import socket
import threading

DAMIY = ["devamEt", "acilFren", "baslat", "yavaşla"]

server_address = ('172.20.10.7', 81)  # Raspberry Pi'nin IP adresini buraya yazın

# Soket oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlan
client_socket.connect(server_address)


def write():
    while True:
        for data in DAMIY:
            if data:
                client_socket.sendall(data.encode())
                # Veri gönderimleri arasında biraz bekleme ekleyebiliriz
                threading.Event().wait(1)

def read():
    while True:
        try:
            # Sunucudan veri al
            received_data = client_socket.recv(1024).decode()
            if received_data:
                print("Alınan Veri (server):", received_data)
            else:
                # Bağlantı kapandıysa döngüyü kır
                break
        except ConnectionResetError:
            # Bağlantı aniden kesilirse döngüyü kır
            break

# Yazma ve okuma iş parçacıklarını başlat
threadWrite = threading.Thread(target=write)
threadRead = threading.Thread(target=read)

threadWrite.start()
threadRead.start()

threadWrite.join()
threadRead.join()

# Bağlantıyı kapat
client_socket.close()