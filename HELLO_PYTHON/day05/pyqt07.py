import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
    
    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        rnd = random();
        if rnd < 0.33:
            com = "가위"
        elif rnd >=0.33 and rnd <=0.66: 
            com = "바위"
        else:
            com = "보"
        
        if mine == "보" and com == "가위": result="짐"
        if mine == "보" and com == "바위": result="이김"
        if mine == "보" and com == "보": result="비김"
        
        if mine == "가위" and com == "가위": result="비김"
        if mine == "가위" and com == "바위": result="짐"
        if mine == "가위" and com == "보": result="이김"
        
        if mine == "바위" and com == "가위": result="이김"
        if mine == "바위" and com == "바위": result="비김"
        if mine == "바위" and com == "보": result="짐"
        
        # if mine==com:
        #     result = "비김"
        # elif (mine=="가위" and com=="보") or (mine=="바위" and com=="가위") or (mine=="보" and com=="바위"):
        #     result = "이김"
        # else:
        #     result = "짐"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()