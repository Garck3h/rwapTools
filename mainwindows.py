#coding=utf-8




from PyQt5 import QtCore, QtGui, QtWidgets
import dmsql_function
import system_function
import rsas_function
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 497)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(83, 187, 98);")

        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 321, 71))

        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lousao = QtWidgets.QPushButton(self.centralwidget)
        self.lousao.setGeometry(QtCore.QRect(40, 190, 141, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.lousao.setFont(font)
        self.lousao.setObjectName("lousao")
        self.lousao.clicked.connect(lambda: self.Rsas_Jx_onButtonClick())
        #self.lousao.clicked.connect(lambda:self.lousao_onButtonClick()) #点击信号,因为show()函数是该主调用程序的外部函数，所以需要使用lambda进行定义


        self.caozuoxitong = QtWidgets.QPushButton(self.centralwidget)
        self.caozuoxitong.setGeometry(QtCore.QRect(250, 190, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.caozuoxitong.setFont(font)
        self.caozuoxitong.setObjectName("caozuoxitong")
        self.caozuoxitong.clicked.connect(lambda: self.System_Jx_onButtonClick())


        self.dmsql = QtWidgets.QPushButton(self.centralwidget)
        self.dmsql.setGeometry(QtCore.QRect(550, 190, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.dmsql.setFont(font)
        self.dmsql.setObjectName("dmsql")
        self.dmsql.clicked.connect(lambda: self.dmsql_onButtonClick())  # 点击信号,因为show()函数是该主调用程序的外部函数，所以需要使用lambda进行定义


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "入网安评工具V1.0_By_Garck"))
        self.label.setText(_translate("MainWindow", "欢迎使用基线工具"))
        self.lousao.setText(_translate("MainWindow", "漏扫结果整理"))
        self.caozuoxitong.setText(_translate("MainWindow", "操作系统基线结果整理"))
        self.dmsql.setText(_translate("MainWindow", "达梦数据库基线"))

    def dmsql_onButtonClick(self):#显示数据库模块的方法
        self.new_window = dmsql_function.Show_Main()
        self.new_window.show()

    def System_Jx_onButtonClick(self):
        self.new_window = system_function.Show_Main()
        self.new_window.show()

    def Rsas_Jx_onButtonClick(self):
        self.new_window = rsas_function.Show_Main()
        self.new_window.show()






