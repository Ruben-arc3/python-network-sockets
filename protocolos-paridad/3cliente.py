# Ejercicio de Telemática: cliente o servidor de sockets (3cliente.py).
import socket

server_host = '127.0.0.1' 
server_port = 12000  

id_cliente = '1001'  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_host, server_port))
    
    client_socket.sendall(id_cliente.encode())
    
    respuesta = client_socket.recv(1024)
    print(f'Respuesta del servidor:\n{respuesta.decode()}')

finally:
    client_socket.close()


