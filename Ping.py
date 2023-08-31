import socket
import sys

# Recebe parâmetros
END_PONG = sys.argv[1]
PORT_PONG = sys.argv[2]
PORT_PING = sys.argv[3]
HOST = "localhost"

#-------------------------------------------#
#        AF_INET = protocolos IPv4          #
#   TCP = SOCK_STREAM / UDP = SOCK_DGRAM    #
#-------------------------------------------#

# Cria um socket datagrama UDP
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cria um socket TCP 
TCP_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

# Monta mensagem de ping
msg_de_ping = str(END_PONG) + ':' + str(PORT_PONG)

# Envia mensagem de ping
UDP_sock.sendto(bytes(msg_de_ping), 'UTF-8')
print("Mensagem de ping enviada")

# Liga o socket TCP ao porto_ping
TCP_sock.bind((HOST, PORT_PING))
# Prepara o socket para receber conexões
TCP_sock.listen()
print("Aguardando conexão do Ping")

# Prepara para aceitar a conexão TCP vinda do Pong
conn,endereco = TCP_sock.accept()
print("Conectado com: ", endereco)

# Espera pela mensagem de Pong 
while True:
    data = conn.recv(1024) #Recebe mensagem
    if not data: #Verifica se acabou de receber os dados
        print("Fechando a conexão")
        conn.close()
        break
    
    # Extrai mensagem recebida
    print(data)
    print("Tamanho mensagem: ", len(data))

# Fecha as conexões
UDP_sock.close()
TCP_sock.close()