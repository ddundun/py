import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def makefile(self):
        print("기본파일생성")
        
    def manjumfn(self):
        print("만점")

    def initUi(self):
        self.filebtn = QPushButton("파일만들기")
        self.manjumbtn = QPushButton("퀴즈2 만점만들기")


        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.filebtn)
        self.hbox.addWidget(self.manjumbtn)
        self.hbox.addStretch(1)
        
        # 세로로된 레이아웃 만들기
        self.vbox = QVBoxLayout()

        # 세로로된 레이아웃에 버튼 넣기
        self.vbox.addStretch(5)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1) #3:1비율

        # self.vbox.addLayout(self.filebtn) -> 가로로두개
        # self.vbox.addLayout(self.manjumbtn) -> 가로로두개


        self.setLayout(self.vbox)
        self.setWindowTitle("FirstApp")
        self.move(300,300)
        self.resize(200,200)
        self.show()

        # 버튼에 이벤트 닫기
        self.filebtn.clicked.connect(self.makefile)
        self.manjumbtn.clicked.connect(self.manjumfn)

if __name__== '__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
