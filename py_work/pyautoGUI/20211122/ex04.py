import time
import pyautogui

aa= pyautogui.locateOnScreen('aa.png', confidence = 0.8)
pyautogui.click(aa)
print(aa)

time.sleep(1)
bb=pyautogui.locateOnScreen('bb.png', confidence = 0.8)
pyautogui.click(bb)
print(bb)

time.sleep(1)
cc=pyautogui.locateOnScreen('cc.png', confidence = 0.8)
pyautogui.click(cc)
print(cc)