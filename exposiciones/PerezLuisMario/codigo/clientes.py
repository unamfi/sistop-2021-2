import socket
from threading import Thread

PORT = 5000
NUM_CLIENTS =  10

def start_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', PORT))
    chunks = []
    bytes_received = 0
    while bytes_received < 18: 
        chunk = client_socket.recv(min(18 - bytes_received, 2048))
        if chunk == b'':
            raise RuntimeError('Socket connection broken')
        chunks.append(chunk)
        bytes_received += len(chunk)
    client_socket.close()
    print(b''.join(chunks))

if __name__ == '__main__':
    for client_id in range(NUM_CLIENTS):
        client = Thread(target = start_connection)
        client.start()