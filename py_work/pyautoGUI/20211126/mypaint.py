
import pyautogui
import time
import pyperclip
from openpyxl import Workbook
from PyQt5.QtWidgets import *

def fontcopy(text):
    pyperclip.copy(text)

def doms():
    try:
        time.sleep(1)
        pyautogui.hotkey("win","r")
        pyautogui.write('mspaint')
        pyautogui.hotkey('enter')
        time.sleep(1)

        box= pyautogui.locateOnScreen('font.png')
        pyautogui.click(box)
        pyautogui.move(10,200,duration =1)
        pyautogui.click()
        fontcopy('참잘했어요')
        pyautogui.hotkey('ctrl','v')

        mywindow = pyautogui.getActiveWindow()
        mywindow.close()
        time.sleep(1)
        pyautogui.write('n')

        wb = Workbook()
        ws = wb.active

        count = ws['A1'].value
        if count == None:
            count ='1'
        else:
            count = int(count)+1

        wb.save('score.xlsx')
        wb.close()

    except Exception as e :
        print(e)

doms()
