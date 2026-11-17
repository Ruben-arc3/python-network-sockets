# Ejercicio de Telemática: cliente o servidor de sockets (1cliente.py).
import socket

def main():
    serverName = "127.0.0.1" 
    serverPort = 12000    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    clientSocket.connect((serverName, serverPort))
    
    msg = input("Ingrese una cadena de dígitos binarios: ")
    
    clientSocket.send(msg.encode('utf-8'))
    
    resultado_paridad = clientSocket.recv(1024).decode('utf-8')
    
    print("Respuesta del servidor:", resultado_paridad)
    
    clientSocket.close()

if __name__ == "__main__":
    main()


