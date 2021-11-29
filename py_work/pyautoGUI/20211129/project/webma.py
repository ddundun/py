from selenium import webdriver
import time

# chrom = webdriver('')
def browserclick(browser,url):
        browser.find_element('xpath',url).click()

def dostart(id,pw):
    print(id)
    print(pw)
    print('일로오나')
    browser = webdriver.Chrome()

    browser.get('https://kb.step.or.kr/main.do')
    time.sleep(1.5)
    ele = browser.find_elemet('xpath','/html/body/section[1]/header/div[2]/div[1]/div/div/div[3]/ul/li[1]/a')
    ele.click()
    time.sleep(1.5)

    browser.find_element('xpath','/html/body/div/div[1]/div/div/div/div[2]/input[1]').send_keys(id)
    browser.find_element('xpath','/html/body/div/div[1]/div/div/div/div[2]/input[2]').send_keys(pw)
    time.sleep(5)

    browser.close()
    browser.quit()
