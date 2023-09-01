import socket
import sys

# Recebe parâmetros
END_PONG = sys.argv[1]
PORT_PONG = int(sys.argv[2])
PORT_PING = int(sys.argv[3])
HOST = 'localhost'

# print("End Pong:", END_PONG)
# print("Porta Pong:", PORT_PONG)

#-------------------------------------------#
#        AF_INET = protocolos IPv4          #
#   TCP = SOCK_STREAM / UDP = SOCK_DGRAM    #
#-------------------------------------------#

# Cria um socket datagrama UDP
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cria um socket TCP 
TCP_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# Liga o socket TCP ao porto_ping
TCP_sock.bind((HOST, PORT_PING))
# Prepara o socket para receber conexões
TCP_sock.listen()
print("Aguardando conexão do Ping...")

# Monta mensagem de ping e envia para o pong
msg_de_ping = HOST + ':' + str(PORT_PING)
UDP_sock.sendto(bytes(msg_de_ping, 'UTF-8'), (END_PONG, PORT_PONG))
# print("Mensagem de ping enviada")

# Prepara para aceitar a conexão TCP vinda do Pong
conn,endereco = TCP_sock.accept()
print("Conectado com: ", endereco)

data = ""
# Espera pela mensagem de Pong 
while True:
    data = conn.recv(1024) #Recebe mensagem
    if not data: #Verifica se acabou de receber os dados
        print("Não há mensagens")
        break
    
    # Extrai mensagem recebida
    print("Mensagem Pong: ",data.decode('UTF-8'))
    print("Tamanho mensagem: ", len(data))

# Fecha as conexões
UDP_sock.close()
TCP_sock.close()