import socket

IP = "127.0.0.1"
PORT1 = 8081
PORT2 = 8082
PORT3 = 8083
PORT4 = 8084

def isConnection(conn):
    # Checando se o cliente está online
    isConnected = "connected?"
    conn.send(isConnected.encode("utf-8"))
    isConnected = conn.recv(1024).decode("utf-8") 

    if isConnected == "Online":
        return True
    else:
        return False

def multiplicacao(numbers):
    return int(numbers[0]) * int(numbers[1])
           

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Conectando ao servidor primário")

    try:
        server.bind((IP, PORT1))
        server.listen()
        print(f"Servidor primário na porta {PORT1}")
    except:
        return print("Problema de conexão. Não foi possível inicializar o Servidor Primário!")

    conn, addr = server.accept()

    nameServidor = conn.recv(1024).decode("utf-8")
    print(nameServidor + " o servidor primário")

    #Verifica se o cliente está online antes de iniciar
    if isConnection(conn):
        numbers = conn.recv(1024).decode("utf-8")
        print(multiplicacao(numbers))

    # conn.close()

if __name__ == "__main__":
    main()