import socket
import os

def main():
    while True:
        server_address = ('localhost', 80)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect(server_address)

            while True:
                with open("client.txt", "r") as file:
                    data = file.read()
                client_socket.sendall(data.encode())

                received_data = client_socket.recv(1024).decode()
                print("Alınan Veri (server):", received_data)
                open("client.txt", "w").close()

                while os.path.getsize("client.txt") == 0:
                    pass
        except ConnectionRefusedError:
            print("Bağlantı reddedildi.")

        client_socket.close()

if __name__ == "__main__":
    main()
