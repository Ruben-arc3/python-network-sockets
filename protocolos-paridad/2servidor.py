# Ejercicio de Telemática: cliente o servidor de sockets (2servidor.py).
import socket

host = '127.0.0.1'  
port = 12000  

limite_venta = 1000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(1)

print(f'Servidor escuchando en {host}:{port}...')

while True:
    client_socket, client_address = server_socket.accept()
    
    print(f'¡Conexión establecida desde {client_address}!')

    try:
        data = client_socket.recv(1024)
        if not data:
            break
        
        mensaje = data.decode()
        detalles = mensaje.split(',')
        articulo = detalles[0]
        precio = float(detalles[1])
        
        if precio > limite_venta:
            respuesta = f'La venta del artículo {articulo} por {precio:.2f} supera el límite permitido de {limite_venta:.2f}'
        else:
            respuesta = f'¡Venta del artículo {articulo} por {precio:.2f} registrada correctamente!'
        
        client_socket.sendall(respuesta.encode())
    
    finally:
        client_socket.close()

server_socket.close()


