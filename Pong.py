import socket
import sys

##---------------------------------Socket UDP---------------------------------##

UDP_HOST   = "127.0.0.1"
UDP_PORT = 20001 #sys
mensagem_entrada ="OLa mundo" #sys

UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_sock.bind((UDP_HOST, UDP_PORT))

while(True):
    bytesAddressPair = UDP_sock.recvfrom(4096)
    mensagem = bytesAddressPair[0]
    endereco = bytesAddressPair[1]

    #Extrai mensagem recebida
    ## Mensagem recebida: IP:porta do ping
    print(mensagem)
    mensagem_separada = mensagem.decode("UTF-8").split(":")
    IP_Ping = mensagem_separada[0]
    Port_Ping = mensagem_separada[1]
    print(IP_Ping)
    print(Port_Ping)
    
    break

##---------------------------------Socket TCP---------------------------------##

TCP_HOST = IP_Ping
TCP_PORT = Port_Ping

TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
TCP_sock.connect((TCP_HOST,TCP_PORT)) #conecta o socket no servidor
TCP_sock.sendall(str.encode(mensagem_entrada)) #Envia mensagem

TCP_sock.close()

UDP_sock.close()