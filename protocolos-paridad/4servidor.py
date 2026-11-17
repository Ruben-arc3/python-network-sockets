# Ejercicio de Telemática: cliente o servidor de sockets (4servidor.py).
import socket

def calcular_suma_n_numeros(n):
    return n * (n + 1) // 2

def main():
    serverPort = 12000
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    serverSocket.bind(("", serverPort))
    
    print("El servidor UDP está listo para recibir...")
    
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)

        try:
            n = int(message.decode('utf-8').strip())
            if n < 0:
                raise ValueError
        except (UnicodeDecodeError, ValueError):
            serverSocket.sendto(
                "Error: ingrese un número natural mayor o igual a 0.".encode('utf-8'),
                clientAddress,
            )
            continue

        print(f"Recibido n = {n} desde {clientAddress}")
        suma = calcular_suma_n_numeros(n)
        serverSocket.sendto(str(suma).encode('utf-8'), clientAddress)

if __name__ == "__main__":
    main()


