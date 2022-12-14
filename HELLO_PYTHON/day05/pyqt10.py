import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.com = "123"
        self.setCom()

    def setCom(self):
        arr9 = [1,2,3,4,5,6,7,8,9]
        for i in range(100):
            rnd = int(random()*9)
            a = arr9[0]
            b = arr9[rnd]
            arr9[0] = b;
            arr9[rnd] = a;
        
        self.com = str(arr9[0]) + str(arr9[1]) + str(arr9[2])
        # print("self.com" ,self.com)
        
    def myclick(self):
        str_old = self.te.toPlainText()
        mine = self.le.text()
        s = self.getStrike(self.com, mine)
        b = self.getBall(self.com, mine)
        str_new = mine + "->" + str(s) + "S" + str(b) + "B" + "\n"
        
        self.te.setText(str_old + str_new)
        self.le.setText("")
        
        if s == 3:
            QMessageBox.about(self,'야구게임',mine + " 를 맞췄습니다")
    
    
    def getStrike(self,com,mine):
        cnt = 0
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]

        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        
        if m1 == c1: cnt += 1
        if m2 == c2: cnt += 1
        if m3 == c3: cnt += 1
        
        return cnt
    
    def getBall(self, com, mine):
        cnt = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        if m1 == c2 or m1 == c3 : cnt +=1
        if m2 == c1 or m2 == c3 : cnt +=1
        if m3 == c1 or m3 == c2 : cnt +=1
        return cnt
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()