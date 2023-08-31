import socket
import sys

# Recebe parâmetros
UDP_HOST = sys.argv[1] #Endereço Pong
UDP_PORT = sys.argv[2] #Porto Pong

TCP_HOST = "localhost"
TCP_PORT = sys.argv[3] #Porto Ping

# Cria um socket datagrama UDP
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#UDP_sock.bind((UDP_HOST, UDP_PORT))

# Cria um socket TCP 
TCP_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # (TCP = SOCK_STREAM/UDP = SOCK_DGRAM)

# Liga o socket TCP ao porto_ping
TCP_sock.bind((TCP_HOST, TCP_PORT))
# Prepara o socket para receber conexões
TCP_sock.listen()
print("Aguardando conexão do Ping")

# Monta mensagem de ping
IP_local_Ping =socket.gethostbyname(socket.gethostname())
msg_de_ping = str(IP_local_Ping) + ':' + str(TCP_PORT)

# Envia mensagem de ping
UDP_sock.sendto(str.encode(msg_de_ping), UDP_HOST)

# Prepara para aceitar a conexão TCP vinda do Pong
conn,endereco = TCP_sock.accept()

# Espera pela mensagem de Pong 
while True:
    data = conn.recv(4096) #Recebe mensagem
    # Extrai mensagem recebida
    print(data)
    print("Tamanho mensagem: ", len(data))
    if not data: #Verifica se acabou de receber os dados
        print("Fechando a conexão")
        conn.close()
        break
    conn.sendall(data) #Envia de volta os dados para o cliente