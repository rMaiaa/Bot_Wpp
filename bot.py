import pywhatkit
import keyboard
import time
from datetime import datetime 

contatos=["+5524998187771"]
contatos2=["+5524998800736"]
contatos3=["+5524999271112"]

while len(contatos) >= 1:

    pywhatkit.sendwhatmsg(contatos[0],contatos2[0],contatos3[0],'aleatorio', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0],contatos2[0],contatos3[0]
    time.sleep(30)
    keyboard.press_and_release('ctrl', 'w')
