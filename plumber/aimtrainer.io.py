import os, sys
import pyautogui as bot
import time
import keyboard
import threading



def killme():
    if keyboard.read_key() == "q":
        print("Bye ..........")
        os._exit(0)

def find():
    location = bot.locateCenterOnScreen("big.png", region=(669, 445, 450, 450))
    print(location)
    if location != None:
        bot.click(location)

threading.Thread(target=killme, name="killer").start()

while True:
    find()