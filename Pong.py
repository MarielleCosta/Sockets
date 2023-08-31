import socket
import sys

# Recebe parâmetros 
UDP_HOST   = "127.0.0.1"
UDP_PORT = sys.argv[1]  #Porto Pong
msg_de_pong = sys.argv[2]   #String Pong

# Cria um socket UDP
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liga o socket ao porto Pong
UDP_sock.bind((UDP_HOST, UDP_PORT))

# Espera uma mensgaem msg_de_ping
while(True):
    bytesAddressPair = UDP_sock.recvfrom(4096)
    mensagem = bytesAddressPair[0]
    endereco = bytesAddressPair[1]

    # Extrai mensagem recebida
    ## Mensagem recebida: IP:porta do ping
    print(mensagem)
    mensagem_separada = mensagem.decode("UTF-8").split(":")
    IP_Ping = mensagem_separada[0]
    Port_Ping = mensagem_separada[1]
    print(IP_Ping)
    print(Port_Ping)
    
    break

# Associa o IP e a porta Ping
TCP_HOST = IP_Ping
TCP_PORT = Port_Ping

# Cria um socket TCP
TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket TCP no Ping
TCP_sock.connect((TCP_HOST,TCP_PORT)) 

# Envia mensagem msg_de_pong
TCP_sock.sendall(str.encode(msg_de_pong))

# Fecha as conexões
UDP_sock.close()
TCP_sock.close()