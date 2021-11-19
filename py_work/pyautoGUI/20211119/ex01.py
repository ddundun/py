import time

import pyautogui

# move: 현재 좌표에서 10,100만큼 이동
# pyautogui.move(10,100,duration =1)

# moveTo: 절대 좌표에서 10,100만큼 이동
# pyautogui.moveTo(10,100,duration =1)

# 현재 좌표 가져오기
pos = pyautogui.position()
print(pos)

pyautogui.click(20,1050,duration =1)
time.sleep(1)
pyautogui.click(389,599,duration =1) 