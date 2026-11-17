# Ejercicio de Telemática: cliente o servidor de sockets (cliente.py).
from socket import *

serverIP = "127.0.0.1" 
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

mensaje = input("Ingresa el mensaje a enviar: ")
clientSocket.sendto(mensaje.encode(), (serverIP, serverPort))

respuesta, servidor = clientSocket.recvfrom(2048)
print(f"Mensaje modificado recibido del servidor: {respuesta.decode()}")

clientSocket.close()



