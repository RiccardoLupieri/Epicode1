
import socket

HOST = '192.168.66.112'  # Indirizzo IP del server
PORT = 7777 # Porta del server

#Crea un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connettiti al server
client_socket.connect((HOST, PORT))

#Invia dati al server
data = 'Ciao server!'
client_socket.sendall(data.encode())

#Ricevi la risposta dal server
response = client_socket.recv(1024)
print('Risposta dal server:', response.decode())
while True:
    command = input('Enter Command : ')
    command = command.encode()
    client_socket.send(command)
    print('[+] Command sent')
    output = client_socket.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
#Chiudi la connessione
client_socket.close()

#Invia un messaggio in Lounge
