# Ejercicio de Telemática: cliente o servidor de sockets (servidor.py).
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(("", serverPort))

print("El servidor está listo para recibir peticiones")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Mensaje recibido: " + message.decode())

    modifiedMessage = message.decode().upper()
    print("Mensaje modificado: " + modifiedMessage)

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Se envió mensaje modificado al cliente")


