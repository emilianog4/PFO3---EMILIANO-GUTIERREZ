import socket

HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor

def enviar_tarea():
    # Crear el socket del cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PORT))
        print("[CONECTADO] Conexión establecida con el servidor.")
        
        # Ingresar una tarea por consola
        tarea = input("Ingresa la tarea a enviar al sistema: ")
        
        # Enviar la tarea codificada en bytes
        cliente.sendall(tarea.encode('utf-8'))
        
        # Recibir la respuesta procesada
        respuesta = cliente.recv(1024).decode('utf-8')
        print(f"\n[RESPUESTA DEL SERVIDOR]: {respuesta}")
        
    except ConnectionRefusedError:
        print("[ERROR] No se pudo conectar al servidor. Asegúrate de que `servidor.py` esté encendido.")
    finally:
        cliente.close()

if __name__ == '__main__':
    enviar_tarea()