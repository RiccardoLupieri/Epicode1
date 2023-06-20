import socket
import codecs

HOST = '192.168.90.101'  # Indirizzo IP del server
PORT = 7777  # Porta del server

#Crea un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connettiti al server
client_socket.connect((HOST, PORT))

#Codifica dei caratteri
encoding = 'cp1252'  # Codifica Windows-1252

#Invia dati al server
data = 'Ciao server!'
data = codecs.encode(data, encoding)
client_socket.sendall(data)

#Ricevi la risposta dal server
response = client_socket.recv(1024)
response = codecs.decode(response, encoding)
print('Risposta dal server:', response)

while True:
    command = input('Enter Command : ')
    command = codecs.encode(command, encoding)
    client_socket.send(command)
    print('[+] Command sent')
    output = client_socket.recv(1024)
    output = codecs.decode(output, encoding)
    print(f"Output: {output}")

#Chiudi la connessione
client_socket.close()

#Invia un messaggio in Lounge
