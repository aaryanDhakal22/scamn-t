import pyautogui
from time import sleep
from random import choice
sleep(3)

names = open("names.txt","r").readlines()
names = [i[:-1] for i in names]
passwords = open("pass.txt",'r').readlines()
passwords = [i[:-1] for i in passwords if passwords.index(i) % 2 == 0]

for i in range(100):
    print("hehe :) ")
    pyautogui.click()
    nametotake = names[i+100]
    passtotake = choice(passwords)
    if len(passtotake) < 8:
        passtotake = nametotake[:nametotake.index('.')] +passtotake
    pyautogui.write(nametotake)
    pyautogui.press("TAB")
    pyautogui.write(passtotake)
    pyautogui.press("ENTER")
    sleep(1)
    with pyautogui.hold('alt'):
        pyautogui.press('left')

    print(nametotake)
    print(passtotake)
    print("Done\n\n")
    sleep(6)