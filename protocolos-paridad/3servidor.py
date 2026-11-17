# Ejercicio de Telemática: cliente o servidor de sockets (3servidor.py).
import socket

archivo_reservas = 'reservas_gimnasio.txt'

def buscar_reservas(id_cliente):
    reservas_cliente = []
    with open(archivo_reservas, 'r') as file:
        for linea in file:
            partes = linea.strip().split(',')
            if partes[0] == id_cliente:
                reservas_cliente.append((partes[1], partes[2]))  
    return reservas_cliente

host = '127.0.0.1'  
port = 12000 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen(1)

print(f'Servidor escuchando en {host}:{port}...')

while True:
    client_socket, client_address = server_socket.accept()
    
    print(f'¡Conexión establecida desde {client_address}!')

    try:
        id_cliente = client_socket.recv(1024).decode().strip()
        
        reservas_cliente = buscar_reservas(id_cliente)
        
        if reservas_cliente:
            respuesta = f'Reservas encontradas para el cliente {id_cliente}:\n'
            for clase, hora in reservas_cliente:
                respuesta += f'- Clase: {clase}, Hora: {hora}\n'
        else:
            respuesta = f'No hay reservas asociadas al cliente {id_cliente}.\n'
        
        client_socket.sendall(respuesta.encode())
    
    finally:
        client_socket.close()

server_socket.close()


