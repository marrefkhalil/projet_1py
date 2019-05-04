# coding: utf-8



# U0=25
#for n in range (0,15):
#   Un1=[12+U0]-[7*n]
#   U0=Un1
#
import requests
from bs4 import BeautifulSoup
import re
session = requests.session() # pour garder les même coockies et la même session
Req = session.get("http://challenge01.root-me.org/programmation/ch1/") # récupérer la page
contenu = Req.content 
formule = re.a= re.findall(r"\[.*", contenu) # récupérer la formule de la suite dans une liste
formule = str(formule[0]).split(" ") # convertir la liste en chaîne de caractère et décomposer la chaine dans une liste de caracètre
a = int(formule[1]) # récupérer le premier paramètre de la suite et le convertir en integer
operation = str(formule[5]) #récupérer l'opération entre les deux crochet et la convertir en string
b = int(formule[9]) #récupérer le troisième paramètre de la suite et le convertir en integer

expRe = re.findall(r"<sub>0</sub>.*", contenu) # récupérer A0
U0 = str(expRe[0]).split(' ')
U0 = int(U0[-1]) # convertir en integer 
print(a, b, operation, U0)

htmlsoup = BeautifulSoup(contenu) # récupérer le contenue de la page pour le pouvoir parser en html à l'aide de beautifulsoup
sub = htmlsoup.find_all('sub') # récupérer toute les balise <sub> et leur contenu
N_EntreSub = str(sub[-1]) # convertir le contenue de la derniere valeur de la liste contenant les sub en string

expRe = re.findall(r">.*<", N_EntreSub) # récupérer A0
N_brute = str(expRe[0])

N_brute = N_brute.split('<') #éliminer <

N_brute2 = N_brute[0].split('>')#éliminer >

n=int(N_brute2[1]) # récupérer n en integer 

########## Calculer la suite 


for x in range(0, n):
    if operation == '-':
        U0=(a+U0)-(b*x)
       # U0=Un1
       # print('dans le - ',U0)
    elif operation == '+' : 
        U0=(a+U0)+(b*x)
       # U0=Un1
       # print('dans le + ',U0)

print(U0)
param = {'result':U0} # paramètre à envoyer en GET(à récupérer sur root me ) 
url=('http://challenge01.root-me.org/programmation/ch1/ep1_v.php')

Reponse = session.get(url, params=param)

print(Reponse.content)
print(Reponse)
print(Reponse.headers)