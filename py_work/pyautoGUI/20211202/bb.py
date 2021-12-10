import pyautogui

x,y = pyautogui.position()
print(x,y)

# //810 290 1118 291

img2 = pyautogui.screenshot('region.png', region=(810,290,316,417))