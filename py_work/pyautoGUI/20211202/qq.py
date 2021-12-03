import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from urllib import parse, request

form_class = uic.loadUiType("dmdkdk.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('images/2.png'))
        self.setupUi(self)

        self.searchbtn.clicked.connect(self.searchfn)




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
        self.label_1.setText('현재날씨 '+w1)
        print('현재날씨 = ', w1)
        w2 = w1.split()

        w3 = w2[2].split('온도')

        w4 = w3[1].split('°')

        if (int(w4[0]) >= 10):
            print("오늘 가디건챙기세요")
            self.label_2.setText("오늘가디건챙기세요")

        elif (int(w4[0]) <= 10):
            self.label_2.setText("롱패딩추천")
            print("롱패딩추천")
            
            # self.label.setText("으아아")
            self.label.setPixmap(QPixmap("3.png"))
            self.show()
    




if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()