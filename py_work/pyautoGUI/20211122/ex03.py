import pyautogui
import time

pyautogui.PAUSE =1 #1초씩 쉬어달라하기
#
# for i in range(5):
#     pyautogui.move(100,100)
#
# img = pyautogui.screenshot()
#
# img.save('a.png')

for i in range(5):
    time.sleep(1) #1초씩 쉬어가면서
    x,y =(pyautogui.position()) #좌표값의 색
    pi = pyautogui.pixel(x,y)
    print('r,g,b',pi) #r g b

