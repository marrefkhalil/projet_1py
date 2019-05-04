# coding: utf-8
import base64
import pytesseract
import requests
from PIL import Image, ImageEnhance, ImageFilter
from bs4 import BeautifulSoup
import re
#pytesseract.pytesseract.tesseract_cmd = '/home/khalil/projetspython/captcha/pytesseract-0.2.5/build/lib.linux-x86_64-2.7/pytesseract'
def convert64toimage(chaine64, pathImage): # fonction pour décoder l'image  coder en base 64 et la mettre dans un fichier png
    
    image = open(pathImage,'wb')
    image_decode = chaine64.decode('base64')
    image.write(image_decode)
    image.close()
    return True

def lireimage(image):
    monimage=Image.open(image)
    tst = pytesseract.image_to_string(monimage)
    return tst
def creationDeSession():
    session = requests.session()
    return session 
def getPage(session,url):
    reponse=session.get(url)
    return reponse
def envoieCode(session,captcha):
    param = {'cametu':captcha}
    reponse = session.post(url, data=param)
    return reponse




url="http://challenge01.root-me.org/programmation/ch8/"
pathImage = 'image.png'
session = creationDeSession()
premiereReponse = getPage(session,url)
contenu = premiereReponse.content
expRe = re.findall(r'base64,.*/><br>', contenu) 
expRe = str(expRe[0]).split('base64,')
expRe = str(expRe[1]).split('" /><br>')
imageBase64 = str(expRe[0])
convert64toimage(imageBase64, pathImage)
captcha = lireimage(pathImage)
reponse = envoieCode(session,captcha)
print(reponse.content)

