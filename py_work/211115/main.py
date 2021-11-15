import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from myExcel import MyExcel

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("assignment.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mex = MyExcel()

        # savebtn loadbtn createbtn
        self.savebtn.clicked.connect(self.savefn)
        self.loadbtn.clicked.connect(self.loadfn)
        self.createbtn.clicked.connect(self.createfn)

    def savefn(self):
        try:
            kor = (self.koredit.text())
            eng = (self.engedit.text())
            math = (self.mathedit.text())
            tot = int(kor) + int(eng) + int(math)
            avg = tot / 3
            print('tot = ', tot)
            print('avg = ', avg)
            self.mex.savefn(kor, eng, math, tot, avg)
        except Exception as e:
            print(e)

    def loadfn(self):
        self.mex.loadfn()

    def createfn(self):
        self.mex.createfn()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()