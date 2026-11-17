# Ejercicio de Telemática: cliente o servidor de sockets (4cliente.py).
import socket

def main():
    serverName = "127.0.0.1"  # Reemplazar con la IP del servidor
    serverPort = 12000
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    n = input("Ingrese un número natural n: ")
    
    clientSocket.sendto(n.encode('utf-8'), (serverName, serverPort))
    
    suma, serverAddress = clientSocket.recvfrom(2048)
    
    print(f"La suma de los primeros {n} números naturales es: {suma.decode('utf-8')}")
    
    clientSocket.close()

if __name__ == "__main__":
    main()


