import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        # print("죽엇나")
        a = self.le1.text()
        b = self.le2.text()
        aa = int(a)
        bb = int(b)
        rs = aa + bb
        # print("죽엇나2")
        self.le3.setText(str(rs))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()