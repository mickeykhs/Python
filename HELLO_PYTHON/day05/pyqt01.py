# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Ui_MainWindow(object):
#     def myclick(self):
#         self.lbl.setText(str("Good Evening"))
#
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(628, 521)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.lbl = QtWidgets.QLabel(self.centralwidget)
#         self.lbl.setGeometry(QtCore.QRect(60, 80, 81, 21))
#         self.lbl.setObjectName("lbl")
#         self.pb = QtWidgets.QPushButton(self.centralwidget)
#         self.pb.setGeometry(QtCore.QRect(190, 80, 75, 23))
#         self.pb.setObjectName("pb")
#         self.pb.clicked.connect(self.myclick)
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.lbl.setText(_translate("MainWindow", "Good Morning"))
#         self.pb.setText(_translate("MainWindow", "click"))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        self.lbl.setText("Good Evening")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()