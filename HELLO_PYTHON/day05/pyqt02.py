import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from asn1crypto.core import Integer

form_class = uic.loadUiType("pyqt02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        # print("죽엇나")  C++ 의 라이브러리를 가져와서 getText()가 아닌 text()이다 결국 C++문법(글자가져오기)
        a = self.le.text()
        # print("죽엇나2")
        rs = int(a)*2
        self.le.setText(str(rs))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()