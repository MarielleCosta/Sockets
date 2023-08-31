import socket
import sys

##---------------------------------Socket UDP---------------------------------##

UDP_HOST = "127.0.0.1" #sys
UDP_PORT = 20001 #sys pong

#Cria um socket datagrama
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#UDP_sock.bind((UDP_HOST, UDP_PORT))
print("Servidor UDP escutando")

##---------------------------------Socket TCP---------------------------------##

TCP_HOST = "localhost"
TCP_PORT = 5000 #sys port pong

TCP_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # (TCP = SOCK_STREAM/UDP = SOCK_DGRAM)
TCP_sock.bind((TCP_HOST, TCP_PORT)) ###Liga o socket TCP ao porto_ping
TCP_sock.listen() ###Prepara o socket para receber conexões
print("Aguardando conexão do Ping")

#####Verificar como montar a mensagem de ping, é de qual endereço Ping ou Pong?
IP_local =socket.gethostbyname(socket.gethostname())
msg_de_ping = str(IP_local) + ':' + str(UDP_PORT)

UDP_sock.sendto(str.encode(msg_de_ping), UDP_HOST)

conn,endereco = TCP_sock.accept() #Retorna o endereço que está conectado

while True:
    data = conn.recv(4096) #Recebe 1024 bytes
    #Extrai mensagem recebida
    ## Mensagem recebida: IP:porta do ping
    print(data)
    print("Tamanho mensagem: ", len(data))
    if not data: #Verifica se acabou de receber os dados
        print("Fechando a conexão")
        conn.close()
        break
    conn.sendall(data) #Envia de volta os dados para o cliente