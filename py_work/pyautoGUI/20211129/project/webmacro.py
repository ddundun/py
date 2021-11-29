from selenium import webdriver

# chrome = webdriver('')

def doStart(id,pw):
    print(id)
    print(pw)
    print('일로온나')
    browser = webdriver.Chrome()

    browser.get('https://kb.step.or.kr/main.do')