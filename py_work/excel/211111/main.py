import sys
from PyQt5.QtWidgets import *
from myExcel import MExcel
# from a import doA

# doA()
# print(__name__)
#
# if __name__ == '__main__':


class MyApp(QWidget):
    # 생성자메서드
    def __init__(self):
        super().__init__()
        # 네모난판떼기
        self.initUi()
        self.m =MExcel()
# '''
#     QLabel : 글자 보여주는 것
#     QLineEdit 글자 입력하는 것
#     QPushButton : 버튼 보여주는 것
# '''

    def initUi(self):
        # btnsave = QPushButton(self)
        # btnsave.setText("저장")
        # btnsave.move(150,30)
        label_1 = QLabel("입력 1",self)
        label_1.move(20,35)
        label_2 = QLabel("입력 2",self)
        label_2.move(20,65)
        label_3 = QLabel("입력 3",self)
        label_3.move(20,95)

        self.lineEdit1 =QLineEdit("aaa",self)
        self.lineEdit1.setFixedSize(65,20)
        self.lineEdit1.move(70,32)

        self.lineEdit2 =QLineEdit("bbb",self)
        self.lineEdit2.setFixedSize(65,20)
        self.lineEdit2.move(70,64)

        self.lineEdit3 =QLineEdit("ccc",self)
        self.lineEdit3.setFixedSize(65,20)
        self.lineEdit3.move(70,96)



        btnsave= QPushButton("저장",self)
        btnsave.move(150, 30)

        btnload = QPushButton(self)
        btnload.setText("불러오기")
        btnload.move(150,60)

        btncreate = QPushButton(self)
        btncreate.setText("Excel 생성")
        btncreate.move(150,90)


        btnsave.clicked.connect(self.btnsavefunc)
        btnload.clicked.connect(self.btnloadfunc)
        btncreate.clicked.connect(self.btncreatefunc)

        self.setWindowTitle("excel 생성, 저장 및 불러오기")
        self.move(300,300)
        self.resize(230,200)
        self.show()
#         좌표 300300 사이즈 400200으로~
# 모듈이름이 메인이면 어저구저쩌구실행

    def btnsavefunc(self):
        # m = MExcel()
        # # ㅇ= ㅇ 객체생성
        a =self.lineEdit1.text()
        b =self.lineEdit2.text()
        c =self.lineEdit3.text()

        self.m.save(a,b,c)

        # self.m.save(self.lineEdit1.text(),
        #             self.lineEdit2.text(),
        #             self.lineEdit3.text())
    def btnloadfunc(self):
        self.m.load()
    def btncreatefunc(self):
        self.m.create()


if __name__== '__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
