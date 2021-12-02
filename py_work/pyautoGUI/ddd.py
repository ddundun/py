# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(1100, 400, 1000, 700)
        self.num = 0

        textLabel = QLabel("res: ", self)
        textLabel.move(20, 20)

        self.label = QLabel(str(self.num), self)
        self.label.move(80, 20)
        self.label.resize(150, 30)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.calc)
        self.timer.start()

    def calc(self):
        self.num += 1
        print(self.num) # 정상실행
        self.label.setText(str(self.num))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    app.exec_()