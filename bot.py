import pywhatkit
import keyboard
import time
from datetime import datetime 

contatos=['INSERIR O NUMERO']

while len(contatos) >= 1:

    pywhatkit.sendwhatmsg(contatos[0],'aleatorio', datetime.now().hour,datetime.now().minute + 1)
    del contatos[0]
    time.sleep(30)
    keyboard.press_and_release('ctrl', 'w')
