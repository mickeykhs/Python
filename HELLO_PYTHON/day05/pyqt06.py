import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from asn1crypto.core import Integer

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        a = self.le.text()
        aa = int(a)
        rs = ""
        # rs += str(aa) + "*1" + "=" + str(aa*1) + "\n"
        # rs += str(aa) + "*2"  + "=" + str(aa*2) + "\n"
        # rs += str(aa) + "*3"  + "=" + str(aa*3) + "\n"
        # rs += str(aa) + "*4"  + "=" + str(aa*4) + "\n"
        # rs += str(aa) + "*5"  + "=" + str(aa*5) + "\n"
        # rs += str(aa) + "*6"  + "=" + str(aa*6) + "\n"
        # rs += str(aa) + "*7"  + "=" + str(aa*7) + "\n"
        # rs += str(aa) + "*8"  + "=" + str(aa*8) + "\n"
        # rs += str(aa) + "*9"  + "=" + str(aa*9) + "\n"
        
        # python 3.5 버전부터 지원가능 fString방식.
        rs += f"{aa}*{1}={aa*1}\n"
        rs += f"{aa}*{2}={aa*2}\n"
        rs += f"{aa}*{3}={aa*3}\n"
        rs += f"{aa}*{4}={aa*4}\n"
        rs += f"{aa}*{5}={aa*5}\n"
        
        rs += f"{aa}*{6}={aa*6}\n"
        rs += f"{aa}*{7}={aa*7}\n"
        rs += f"{aa}*{8}={aa*8}\n"
        rs += f"{aa}*{9}={aa*9}\n"
         
        self.te.setText(rs)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()