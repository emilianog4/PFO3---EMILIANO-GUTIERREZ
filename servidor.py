import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

# Función que procesa cada tarea en un hilo independiente (Simulando un Worker con pool de hilos)
def manejar_tarea(conn, addr):
    print(f"[CONEXIÓN] Cliente conectado desde: {addr}")
    try:
        # Recibir la tarea enviada por el cliente
        data = conn.recv(1024).decode('utf-8')
        if not data:
            return
        
        print(f"[TAREA RECIBIDA] De {addr}: {data}")
        
        # Simular procesamiento de la tarea (como si interactuara con BD o workers)
        resultado = f"Tarea '{data}' procesada exitosamente por el servidor distribuido."
        
        # Enviar el resultado de vuelta al cliente
        conn.sendall(resultado.encode('utf-8'))
        
    except Exception as e:
        print(f"[ERROR] Ocurrió un error con {addr}: {e}")
    finally:
        conn.close()
        print(f"[DESCONEXIÓN] Conexión cerrada con {addr}\n")

def iniciar_servidor():
    # Crear el socket del servidor (TCP/IP)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[SERVIDOR ACTIVO] Escuchando en {HOST}:{PORT}...")

    while True:
        # Aceptar la conexión entrante de un cliente
        conn, addr = servidor.accept()
        
        # Crear un hilo por cada cliente para manejar tareas concurrentemente (Pool de hilos básico)
        hilo_worker = threading.Thread(target=manejar_tarea, args=(conn, addr))
        hilo_worker.start()

if __name__ == '__main__':
    iniciar_servidor()