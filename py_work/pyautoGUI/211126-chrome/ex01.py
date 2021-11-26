import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://www.naver.com')
element = browser.find_element_by_link_text('카페')

print(element.get_attribute('href'))
print(element.get_attribute('class'))

element.click()
time.sleep(1)
browser.back()
time.sleep(1)
browser.refresh() #새로고침

input_ele = browser.find_element_by_id('query')
input_ele.send_keys('초록뱀미디어')

btntag = browser.find_element_by_xpath('//*[@id="search_btn"]')
btntag.click()

browser.save_screenshot('snake.png')
time.sleep(5)
browser.close()