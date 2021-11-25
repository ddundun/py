import pyautogui
import pyperclip

pyautogui.sleep(1)
pyautogui.write('1234')
pyautogui.sleep(1)
pyautogui.write('abcdefg', interval = 0.25)


pyautogui.sleep(1)
# pyautogui.write('한글') 한글은안됨 ㅜ

# 아래방법으로 한글사용 가능
pyperclip.copy('한글')
pyautogui.hotkey('ctrl','v')