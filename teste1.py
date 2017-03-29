from socket import *
import time
 
address = ( '169.254.39.10', 5000) #Defind who you are talking to (must match arduino IP and port)
client_socket = socket(AF_INET, SOCK_DGRAM) #Set Up the Socket
client_socket.settimeout(1) #only wait 1 second for a resonse
 
while(1): #Main Loop
 
    data = "Liga" #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        print( rec_data) #Print the response from Arduino
    except:
        pass
 
    time.sleep(1) #delay before sending next command
 
    data = "Lum" #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Read response from arduino
        print (rec_data) #Print the response from Arduino
    except:
        pass
 
    time.sleep(1) #delay before sending next command
    
    data = "Desliga" #Atribui a palavra "Desliga" para a variável data
    client_socket.sendto(data, address) #envia o comando "Desliga" para o arduino
    try:
        rec_data, addr = client_socket.recvfrom(2048) #Recebe a resposta do arduino
        print (rec_data) #Mostra a resposta recebida do Arduino
    except:
        pass
    time.sleep(1) #Espera 1 segundo para o próximo comando
