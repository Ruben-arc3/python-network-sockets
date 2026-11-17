# Ejercicio de Telemática: cliente o servidor de sockets (servidor.py).
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))

serverSocket.listen(1)
print("El servidor está listo para recibir peticiones:")

while True:
    conSocket, addr = serverSocket.accept()
    print("Recibiendo mensajes desde el cliente", addr)

    msg = conSocket.recv(1024)

    msg_change = msg.upper()

    conSocket.send(msg_change)

    conSocket.close()

serverSocket.close()



