import sys
from PyQt5.QtWidgets import *
import time
import pyautogui

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("FirstApp")
        self.move(300,300)
        self.resize(400,200)
        self.show()

if __name__== '__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
