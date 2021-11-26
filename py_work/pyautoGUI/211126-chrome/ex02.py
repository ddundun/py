## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def webmacro(self):
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
        browser.refresh()  # 새로고침

        input_ele = browser.find_element_by_id('query')
        input_ele.send_keys('초록뱀미디어')

        btntag = browser.find_element_by_xpath('//*[@id="search_btn"]')
        btntag.click()

        browser.save_screenshot('snake.png')
        time.sleep(5)
        browser.close()

        self.lbl_img.setPixmap(QPixmap('snake.png'))

    def initUI(self):
        pixmap = QPixmap('snake.png')

        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(pixmap)

        lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        load_btn = QPushButton('웹매크로')
        load_btn.clicked.connect(self.webmacro)

        hbox = QHBoxLayout()
        hbox.addWidget(lbl_size)
        hbox.addWidget(load_btn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_img)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('QPixmap')
        self.move(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())