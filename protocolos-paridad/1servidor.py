# Ejercicio de Telemática: cliente o servidor de sockets (1servidor.py).
import socket

def calcular_paridad(cadena_binaria):
    cantidad_unos = cadena_binaria.count('1')
    
    if cantidad_unos % 2 == 0:
        return "Paridad correcta: la cantidad de unos es par."
    else:
        return "Paridad incorrecta: la cantidad de unos es impar."

def main():
    serverPort = 12000
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serverSocket.bind(("", serverPort))
    
    serverSocket.listen(1)
    
    print("El servidor está listo para recibir conexiones...")
    
    while True:
        conSocket, addr = serverSocket.accept()
        print(f"Conexión establecida desde {addr}")
        
        msg = conSocket.recv(1024).decode('utf-8')
        print(f"Mensaje recibido del cliente: {msg}")
        
        resultado_paridad = calcular_paridad(msg)
        
        conSocket.send(resultado_paridad.encode('utf-8'))
        
        conSocket.close()

if __name__ == "__main__":
    main()



