import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel()
        label.setPixmap(QPixmap("../20211202/images/2.png"))
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()