import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from bs4 import BeautifulSoup
from urllib import parse, request

form_class = uic.loadUiType("dmdkdk.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('images/2.png'))
        self.setupUi(self)
        self.searchbtn.clicked.connect(self.searchfn)
        self.mywidget = Widgets(self)
        self.setWidget(self.mywidget)


    def searchfn(self):

        d = (self.lineEdit.text())
        d += "날씨"
        d = parse.quote(d)
        URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + d

        source = request.urlopen(URL)
        soup = BeautifulSoup(source.read(), 'html.parser')

        w1 = soup.find("div", {"class": "weather_graphic"})
        # weather = soup.find("ul", {"class": "weather_info_list"})
        w1 = w1.get_text()
        # weather = weather.get_text()
        print('현재날씨 = ', w1)
        w2 = w1.split()

        w3 = w2[2].split('온도')

        w4 = w3[1].split('°')

        if (int(w4[0]) >= 10):
            print('오늘 가디건챙기세용')

        elif (int(w4[0]) <= 5):
            print('롱패딩추천')

class Widgets(QWidget):
    def __init__(self, parent):
        super(Widgets,self).__init__(parent)

        ##### 위젯 함수 실행
        self.initWidget()

    ##### 위젯셋팅
    def initWidget(self):
        label_1 = QLabel("라벨1", self)
        label_2 = QLabel("라벨2", self)
        label_3 = QLabel("라벨3", self)

        ##### 레이이아웃
        boxlayout = QVBoxLayout(self)
        boxlayout.addWidget(label_1)
        boxlayout.addWidget(label_2)
        boxlayout.addWidget(label_3)





if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()