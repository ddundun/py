import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from myExcel import MyExcel

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("assignment1.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.col = 0

        self.value = 1

        self.setupUi(self)
        self.mex = MyExcel()

        self.initUi()  # 화면먼저만들고
        self.savebtn.clicked.connect(self.savefn)
        self.loadbtn.clicked.connect(self.loadfn)
        self.createbtn.clicked.connect(self.createfn)

        self.signalfn()  # 시그널~

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

    def mybtnfn(self):
        self.tablew.setItem(1,0, QTableWidgetItem(str(self.kor)))
        # self.tablew.append(self.kor,self.eng,self.math)
        print("누름")


    def signalfn(self):
        self.savebtn.clicked.connect(self.mybtnfn)

    def loadfn(self):
        self.mex.loadfn()

    def createfn(self):
        self.mex.createfn()

    def initUi(self):
        # self.btn1 = QPushButton("추가", self)
        # self.btn1.move(10, 10)
        self.tablew = QTableWidget(self)  # 테이블 생성 후 Qwidget에 붙이기
        self.tablew.move(10, 300)  # 테이블 x좌표로 100 y좌표로 10에서 그리기
        self.tablew.setRowCount(10)  # 행 개수 10개 지정 (세로)
        self.tablew.setColumnCount(5)  # 컬럼개수 4개 (가로)
        self.tablew.setFixedSize(530, 400)  # 테이블 크기

        self.setWindowTitle("First App")
        self.move(300, 300)
        self.resize(600, 800)
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