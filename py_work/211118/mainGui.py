import sys
from PyQt5.QtWidgets import *
from scoreExcel import ScoreExcel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.se = ScoreExcel() #객체생성
        self.rowIndex =0

        self.initUi() #화면생성
        self.initEvent() #시그널생성 이벤트함수 (클릭?)
        self.loadfile()

    # 조회.. 가져오기 .. #checkbox...
    def loadfile(self):
        rows =self.se.loadrow()
        for row in rows:
            self.qtable.setItem(self.rowIndex,0,QTableWidgetItem(row[0]))
            self.qtable.setItem(self.rowIndex,1,QTableWidgetItem(row[1]))
            self.qtable.setItem(self.rowIndex,2,QTableWidgetItem(row[2]))
            self.qtable.setItem(self.rowIndex,3,QTableWidgetItem(row[3]))
            self.qtable.setItem(self.rowIndex,4,QTableWidgetItem(row[4]))
            self.rowIndex +=1

    def append(self):
        try:
            kor = self.kor_edit.text()
            eng = self.eng_edit.text()
            math = self.math_edit.text()
            tot = int(kor)+int(eng)+int(math)
            avg = int (tot/3 *100) /100 #소수 둘째자리까지 ~
            # 76.666666 *100 -> 7666.66666 -> 7666/100 -> 76.66


            self.qtable.setItem(self.rowIndex,0,QTableWidgetItem(kor))
            self.qtable.setItem(self.rowIndex,1,QTableWidgetItem(eng))
            self.qtable.setItem(self.rowIndex,2,QTableWidgetItem(math))
            self.qtable.setItem(self.rowIndex,3,QTableWidgetItem(str(tot)))
            self.qtable.setItem(self.rowIndex,4,QTableWidgetItem(str(avg)))


            self.se.appendrow(kor,eng,math,str(tot),str(avg))
            self.rowIndex += 1

        except Exception as e:
            print(e)

    def delete(self):
        self.qtable.setItem(self.rowIndex-1, 0, QTableWidgetItem(''))
        self.qtable.setItem(self.rowIndex-1, 1, QTableWidgetItem(''))
        self.qtable.setItem(self.rowIndex-1, 2, QTableWidgetItem(''))
        self.qtable.setItem(self.rowIndex-1, 3, QTableWidgetItem(''))
        self.qtable.setItem(self.rowIndex-1, 4, QTableWidgetItem(''))

        self.se.deleterow(self.rowIndex)
        self.rowIndex -= 1

    def create(self):
       self.se.createfile()


    def initEvent(self):
        self.add_btn.clicked.connect(self.append)
        self.del_btn.clicked.connect(self.delete)
        self.create_btn.clicked.connect(self.create)

    def initUi(self):
        self.qtable = QTableWidget(self)
        # col_labels = ['국어','영어','수학','총점','평균']
        # self.qtable.setHorizontalHeaderLabels(col_labels) 카운트 지정되고해야함

        self.qtable.setRowCount(10)
        self.qtable.setColumnCount(5)

        self.qtable.setHorizontalHeaderLabels(['국어', '영어', '수학', '총점', '평균'])
        self.qtable.horizontalHeader()\
            .setSectionResizeMode(QHeaderView.Stretch)

        self.qtable.move(60,120)
        self.qtable.setFixedSize(540,328)

        kor_label = QLabel("국어",self)
        kor_label.move(50,40)
        eng_label = QLabel("영어",self)
        eng_label.move(50,65)
        math_label = QLabel("수학",self)
        math_label.move(50,90)

        # lineedit은 클래스변수여야하므로 self붙이기
        self.kor_edit = QLineEdit("국어점수",self)
        self.kor_edit.move(100,37)
        self.eng_edit = QLineEdit("영어점수",self)
        self.eng_edit.move(100,62)
        self.math_edit = QLineEdit("수학점수",self)
        self.math_edit.move(100,87)

        self.add_btn = QPushButton("추가",self)
        self.add_btn.move(500,30)
        self.del_btn = QPushButton("삭제",self)
        self.del_btn.move(500,55)
        self.create_btn = QPushButton("파일 생성",self)
        self.create_btn.move(500,80)

        self.setWindowTitle("score pg")
        self.move(300,300)
        self.resize(670,500)
        self.show()

if __name__== '__main__':
    app=QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
