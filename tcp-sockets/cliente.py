# Ejercicio de Telemática: cliente o servidor de sockets (cliente.py).
from socket import *

servername = "127.0.0.1"

serverport = 12000

clienteSocket = socket(AF_INET, SOCK_STREAM)

clienteSocket.connect((servername, serverport))

msg = input("Escriba una palabra: ")

clienteSocket.send(msg.encode('utf-8'))

msg_modified = clienteSocket.recv(1024)

print("El mensaje cambiado es:", msg_modified.decode('utf-8'))

clienteSocket.close()


