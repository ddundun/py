import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
import cv2

form_class = uic.loadUiType("untitled.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.copybtn.clicked.connect(self.copyfn)
        self.redbtn.clicked.connect(self.redfn)
        self.red_allbtn.clicked.connect(self.red_allfn)
        self.graybtn.clicked.connect(self.grayfn)

        pixmap = QPixmap("4.png")
        self.label.setPixmap(QPixmap(pixmap))
        self.label.adjustSize()

    def copyfn(self):
        print("이미지 추출 및 복사")
        a='4.png'
        img = cv2.imread(a, cv2.IMREAD_COLOR)
        cv2.imwrite('444.png', img)
        pixmap = QPixmap("444.png")
        self.label.setPixmap(QPixmap(pixmap))
        self.label.adjustSize()

    def redfn(self):
        print("레드색 제거")
        img = cv2.imread('4.png', cv2.IMREAD_COLOR)
        img[:, :, 2] = 0
        cv2.imwrite('44_red.png', img)
        pixmap = QPixmap("44_red.png")
        self.label.setPixmap(QPixmap(pixmap))
        self.label.adjustSize()

    def red_allfn(self):
        print("레드색전체처리")
        img = cv2.imread('4.png', cv2.IMREAD_COLOR)
        img[:, :,2 ] = 255
        cv2.imwrite('44_redall.png', img)
        pixmap = QPixmap("44_redall.png")
        self.label.setPixmap(QPixmap(pixmap))
        self.label.adjustSize()

    def grayfn(self):
        print("그레이처리")
        img = cv2.imread('4.png', cv2.IMREAD_COLOR)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('44_gray.png', img_gray)
        pixmap = QPixmap("44_gray.png")
        self.label.setPixmap(QPixmap(pixmap))
        self.label.adjustSize()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()