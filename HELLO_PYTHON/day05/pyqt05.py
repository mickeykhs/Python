import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from dask.array.random import randint
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.leMine.returnPressed.connect(self.myclick)
    
    def myclick(self):
        a = self.leMine.text()
        b = ""
        rs = ""
        # rnd = randint(1,10)
        # print(rnd)
        rnd = random()*10
        print(rnd)
        if rnd < 5:
            b = "홀"
        else:
            b = "짝"
        
        if a == b:
            rs = "승리"
        else:
            rs = "패배"
        
        self.leCom.setText(b)
        self.leResult.setText(rs)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()