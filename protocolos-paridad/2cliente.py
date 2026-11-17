# Ejercicio de Telemática: cliente o servidor de sockets (2cliente.py).
import socket

server_host = '127.0.0.1'  
server_port = 12000  

articulo = 'Camisa'
precio = 850.0  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_host, server_port))
    
    mensaje = f'{articulo},{precio}'
    client_socket.sendall(mensaje.encode())
    
    respuesta = client_socket.recv(1024)
    print(f'Respuesta del servidor: {respuesta.decode()}')

finally:
    client_socket.close()


