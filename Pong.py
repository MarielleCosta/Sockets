import socket
import sys

# Recebe parâmetros 
HOST = 'localhost'
PORT_PONG = int(sys.argv[1])
MSG_PONG = sys.argv[2]

# Cria um socket UDP
# AF_INET = protocolos IPv4
# TCP = SOCK_STREAM / UDP = SOCK_DGRAM
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Liga o socket a porta Pong
UDP_sock.bind((HOST, PORT_PONG))

# UDP: Espera uma mensagem do Ping
mensagem = ""
while(True):
    bytesAddressPair = UDP_sock.recvfrom(1024)
    mensagem = bytesAddressPair[0]
    endereco = bytesAddressPair[1]

    clientMsg = "Mensagem do Cliente:{}".format(mensagem)
    clientIP  = "Endereço IP Cliente:{}".format(endereco)
    
    # Extrai mensagem recebida
    ## Mensagem recebida: IP:porta do ping
    if(mensagem != ""):
        print(clientMsg)
        print(clientIP)
        break
    
msg_de_ping = mensagem.decode('UTF-8').split(":")
IP_Ping = endereco[0]
Port_Ping = msg_de_ping[1]
print('IP Ping: ', IP_Ping)
print('Porta Ping: ', Port_Ping)

# Cria um socket TCP
TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket TCP no Ping
TCP_sock.connect((IP_Ping,int(Port_Ping))) 
#TCP_sock.connect((endereco[0],int(Port_Ping))) 

# Envia mensagem msg_de_pong
TCP_sock.sendall(bytes(MSG_PONG, 'utf-8'))

# Fecha as conexões
UDP_sock.close()
TCP_sock.close()