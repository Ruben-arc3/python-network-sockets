# Prácticas de Telemática: sockets en Python

Repositorio de prácticas universitarias de Telemática sobre comunicación cliente-servidor mediante sockets TCP y UDP en Python. Los ejemplos usan únicamente la biblioteca estándar; no requieren paquetes externos. Se recomienda Python 3.8 o posterior.

## Ejecución rápida

Abre dos terminales en la raíz del repositorio. Inicia primero el servidor y luego el cliente en la otra terminal. Deja el servidor activo mientras haces la prueba; detenlo con Ctrl+C.

### TCP: transformación a mayúsculas

Terminal 1: `python tcp-sockets/servidor.py`

Terminal 2: `python tcp-sockets/cliente.py`

Puerto 12000.

### UDP: transformación a mayúsculas

Terminal 1: `python udp-sockets/servidor.py`

Terminal 2: `python udp-sockets/cliente.py`

Puerto 12000. Ejecuta los ejercicios de esta carpeta por separado.

## Prácticas numeradas

Cada práctica requiere dos terminales: ejecuta primero el servidor y luego su cliente. Por ejemplo, para la práctica 1:

Terminal 1: `python protocolos-paridad/1servidor.py`

Terminal 2: `python protocolos-paridad/1cliente.py`

Cambia el número 1 por 2, 3 o 4 para ejecutar las otras prácticas.

| Práctica | Transporte | Descripción | Puerto |
| --- | --- | --- | ---: |
| 1 | TCP | Comprueba la paridad de la cantidad de unos en una cadena binaria. | 12000 |
| 2 | TCP | Valida el precio de un artículo frente a un límite de venta. | 12000 |
| 3 | TCP | Busca reservas por ID en reservas_gimnasio.txt. | 12000 |
| 4 | UDP | Calcula la suma de los primeros n números naturales. | 12000 |

La práctica 3 usa datos de ejemplo en reservas_gimnasio.txt.

## Estructura

- tcp-sockets/: cliente y servidor TCP que convierten texto a mayúsculas.
- udp-sockets/: cliente y servidor UDP que convierten texto a mayúsculas.
- protocolos-paridad/: cuatro ejercicios numerados sobre sockets y protocolos sencillos.

Por defecto, los programas usan 127.0.0.1 para ejecutarse en una sola máquina. Para trabajar entre equipos, cambia la dirección en el cliente y configura el servidor para escuchar en las interfaces de red; puede requerirse una regla en el firewall.

