import time
import pyautogui

aa= pyautogui.locateOnScreen('aa.png', confidence = 0.8)
pyautogui.click(aa)
print(aa)

time.sleep(2)
bb=pyautogui.locateOnScreen('bb.png')
pyautogui.click(bb)
print(bb)