# initqt 복사
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.row = 0
        self.col = 0

        self.value =1

        self.initUi() #화면먼저만들고
        self.signalfn() #시그널~

    # excel저장+ 화면에도 나타나게..
    def mybtnfn(self):
        self.tablew.setItem(self.row,self.col,QTableWidgetItem(str(self.value)))
        print("누름")
        self.value+=1
        # self.row +=1
        self.col +=1
        if(self.col >3): #4이상이되면 밑줄로 >3 or ==4 //0부터시작하기때문에
            self.row +=1
            self.col = 0
        if(self.row >9): #==10
            self.tablew.setRowCount(self.row+1)

    # control 이벤트 다는 곳 // Q위젯들..?전부
    def signalfn(self):
        self.btn1.clicked.connect(self.mybtnfn)

    # 디자인 하는 곳
    def initUi(self):

        self.btn1 = QPushButton("추가",self)
        self.btn1.move(10,10)

        self.tablew = QTableWidget(self) #테이블 생성 후 Qwidget에 붙이기
        self.tablew.move(100,10) # 테이블 x좌표로 100 y좌표로 10에서 그리기
        self.tablew.setRowCount(10) #행 개수 10개 지정 (세로)
        self.tablew.setColumnCount(4) #컬럼개수 4개 (가로)
        self.tablew.setFixedSize(430,400) #테이블 크기


        self.setWindowTitle("First App")
        self.move(300,300)
        self.resize(800,600)
        self.show()

if __name__== '__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
