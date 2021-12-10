import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from project3 import ProjectExcel
from project4 import Typing
from bs4 import BeautifulSoup
from twilio.rest import Client
from urllib import parse, request

form_class = uic.loadUiType("untitled.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchbtn.clicked.connect(self.searchfn)
        self.nextGo.clicked.connect(self.nextGoGo)

    def nextGoGo(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def searchfn(self):

        d = (self.lineEdit.text())
        d += "날씨"
        d = parse.quote(d)
        URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + d

        source = request.urlopen(URL)
        soup = BeautifulSoup(source.read(), 'html.parser')

        w1 = soup.find("div", {"class": "weather_graphic"})
        c1 = soup.find("div", {"class": "temperature_info"})
        n1 = soup.find("ul", {"class": "weather_info_list"})
        m1 = soup.find("ul", {"class": "today_chart_list"})

        if (w1 == None):
            QMessageBox.about(self, "경고", "한국지역만 검색가능^^/이상한거 검색노노")
        else:
            t1 = soup.find("dl", {"class": "info"})
            t2 = t1.find('dd').text.strip()
            t2 = t2.split()
            t2 = t2[:3]
            t2 = ' '.join(t2)
            w1 = w1.get_text()
            n1 = n1.get_text()
            c1 = c1.get_text()
            m1 = m1.get_text()

            self.label_1.setText('현재날씨 ' + w1)
            self.label_1.adjustSize()
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)

            self.label_6.setText(t2 + '기준')
            self.label_6.adjustSize()
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)

            w2 = w1.split()

            c2 = c1.split()
            c3 = c2[4:8]
            c4 = ' '.join(c3)

            m1 = m1.split()
            m1 = m1[:4]
            m2 = ' '.join(m1)

            self.label_3.setText(c4)
            self.label_3.adjustSize()
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)

            self.label_5.setText(m2)
            self.label_5.adjustSize()
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)

            # w3 = w2[2].split('온도')
            # w4 = w3[1].split('°')

            if (w2[0] == '맑음'):
                pixmap = QPixmap("3.png")
                self.label_4.setPixmap(QPixmap(pixmap))
                self.label_4.adjustSize()

                self.show()
            elif (w2[0] == '구름많음'):
                pixmap = QPixmap("1.png")
                self.label_4.setPixmap(QPixmap(pixmap))
                self.label_4.adjustSize()

            if (m1[1] == '나쁨' or m1[3] == '나쁨'):
                self.label.setText("마스크끼세용")
                self.label.adjustSize()
                self.label.setAlignment(QtCore.Qt.AlignCenter)
            else:
                self.label.setText("신선한공기마십시당")
                self.label.adjustSize()
                self.label.setAlignment(QtCore.Qt.AlignCenter)

            w3 = w2[2].split('온도')
            w4 = w3[1].split('°')

            if (int(w4[0]) <= 4):
                self.label_2.setText("패딩 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                self.label_c.setPixmap(QPixmap("4.png"))
                self.label_c.adjustSize()
                self.show()

            elif (int(w4[0]) < 8):
                self.label_2.setText("코트 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("8.png")
                self.label_c.setPixmap(QPixmap(pixmap))
                self.label_c.adjustSize()
                self.show()

            elif (int(w4[0]) < 15):
                self.label_2.setText("자켓 추천")
                self.label_2.adjustSize()
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

                pixmap = QPixmap("9.png")
                self.label_c.setPixmap(QPixmap(pixmap))
                self.label_c.adjustSize()
                self.show()


class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.pe = ProjectExcel()
        loadUi("remake2.ui", self)
        self.sendbtn.clicked.connect(self.nextPage)
        self.previousbtn.clicked.connect(self.backGoGo)
        self.rowIndex = 0
        self.initEvent()
        self.loadfile()

    def backGoGo(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def loadfile(self):
        rows = self.pe.loadrow()
        for row in rows:
            self.tableWidget.setCellWidget(self.rowIndex, 0, QCheckBox())
            self.tableWidget.setItem(self.rowIndex, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(self.rowIndex, 2, QTableWidgetItem(row[2]))
            self.rowIndex += 1

    def push(self):
        checkbox = self.tableWidget.setCellWidget(self.rowIndex, 0, QCheckBox())
        name = self.name_edit.text()
        number = self.number_edit.text()
        self.tableWidget.setItem(self.rowIndex, 0, QTableWidgetItem(checkbox))
        self.tableWidget.setItem(self.rowIndex, 1, QTableWidgetItem(name))
        self.tableWidget.setItem(self.rowIndex, 2, QTableWidgetItem(number))
        self.pe.appendrow("0", name, number)
        self.rowIndex += 1

    def create(self):
        self.pe.createfile()

    def initEvent(self):
        self.push_btn.clicked.connect(self.push)
        self.create_btn.clicked.connect(self.create)

    def nextPage(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SendingMessage(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("page2.ui", self)
        self.backbtn.clicked.connect(self.backbtned)
        self.pushSends.clicked.connect(self.pushGo)
        self.ty = Typing()
        self.loadText()
        self.pe = ProjectExcel()

    def loadText(self):
        message = self.ty.returnMessage()
        self.textEdit.append(message)

    def backbtned(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def pushGo(self):
        rows2 = self.pe.oneside()
        account_sid = 'AC3b85cda197ef102bb4ce500f08b6b996'
        auth_token = '0b6085136084edaf14ceab42f01871eb'
        client = Client(account_sid, auth_token)
        # 보낼 메세지 내용 가져오기
        messageBox = self.textEdit.toPlainText()
        for i in rows2:
            message = client.messages \
                .create(
                body=messageBox,
                from_='+12285919829',
                to='+82' + i[1:11]
            )
        print(message.sid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = WindowClass()
    mainWindow = MyApp()
    sendingPage = SendingMessage()
    widget.addWidget(main)
    widget.addWidget(mainWindow)
    widget.addWidget(sendingPage)
    widget.setFixedHeight(467)
    widget.setFixedWidth(431)
    widget.setWindowIcon(QIcon('2.png'))
    widget.setWindowTitle('날씨의 요정')
    widget.show()
    app.exec_()

