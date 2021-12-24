import pyautogui
import os
import time

print('Scanning for Accept buttons every 1s, press ctrl-c to cancel')

while True:
    #buttonSeeker = pyautogui.locateCenterOnScreen('c:\\Users\\Andy\\accept.png', minSearchTime=2000)
    buttonSeeker = pyautogui.locateCenterOnScreen('c:\\Users\\Andy\\accept.png')
    if(buttonSeeker):
        print('Found game start!')
        pyautogui.moveTo(buttonSeeker)
        pyautogui.click(buttonSeeker)
        pyautogui.click(buttonSeeker)
        pyautogui.moveTo(500,500)
    #else:
     #   print('Game start not found')

    #buttonSeeker2 = pyautogui.locateCenterOnScreen('c:\\Users\\Andy\\party.png', minSearchTime=2000)
    buttonSeeker2 = pyautogui.locateCenterOnScreen('c:\\Users\\Andy\\party.png')
    if(buttonSeeker2):
        print('Found Invite!')
        pyautogui.moveTo(buttonSeeker2)
        pyautogui.click(buttonSeeker2)
        pyautogui.click(buttonSeeker2)
        pyautogui.moveTo(500,500)
    #else:
     #   print('Invite not found')
     
    buttonSeeker3 = pyautogui.locateCenterOnScreen('c:\\Users\\Andy\\ready.png')
    if(buttonSeeker3):
        print('Found Readycheck!')
        pyautogui.moveTo(buttonSeeker3)
        pyautogui.click(buttonSeeker3)
        pyautogui.click(buttonSeeker3)
        pyautogui.moveTo(500,500)

    time.sleep(1)
#end while
