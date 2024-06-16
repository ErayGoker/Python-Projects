import socket
import threading
import random

# Lock nesnesi
lock = threading.Lock()

# Rastgele veriler oluştur
DAMIY = []
for _ in range(100):
    konum = random.randint(0, 100)
    hiz = random.randint(0, 100)
    b_volt = random.uniform(30, 31)
    DAMIY.append((konum, hiz, b_volt))

# Sunucu soketi oluştur ve ayarla
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 81))  # Tüm IP adreslerinden bağlanma izni ver
server_socket.listen(1)  # Bağlantıları dinle

print("Sunucu başlatıldı. İstemciyi bekliyor...")

# İstemci bağlantısını kabul et
client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

# Verileri istemciye gönderme fonksiyonu
def write():
    for x in DAMIY:
        data = str(x)
        client_socket.sendall(data.encode())
        # Veri gönderimleri arasında biraz bekleme ekleyebiliriz, aksi takdirde istemci verileri işleyemeyebilir
        threading.Event().wait(0.1)

# İstemciden veri alma fonksiyonu
def read():
    while True:
        try:
            received_data = client_socket.recv(1024).decode()
            if received_data:
                print("Alınan Veri (client):", received_data)
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
server_socket.close()
