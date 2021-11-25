import time

import pyautogui

fw = pyautogui.getActiveWindow() #현재창가져오기
print(fw.title)
print(fw.size)
print(fw.left,fw.right)

# pyautogui.click(fw.left+60,fw.right+20) #file 메뉴클릭하기

# for fw in pyautogui.getAllWindows(): #모든창가져오기
#     print(fw)
#
# # sleep : 쉬기

fw = pyautogui.getWindowsWithTitle("제목 없음")[0]
if fw.isActive == False:
    fw.activate() 
#     활성화 x ->활성화

if fw.isActive ==True:
    fw.maximize()

time.sleep(3)
fw.restore()
fw.close()
