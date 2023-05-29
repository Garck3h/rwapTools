# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from functools import partial
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 669)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(60,63,65);\n"
"")
        #蓝色：65,124,199
        #灰色：60,63,65
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #####################  标签   #########################
        #disql选择按钮


        #disql选择按钮
        self.disql_button = QtWidgets.QPushButton(self.centralwidget)
        self.disql_button.setGeometry(QtCore.QRect(110, 15, 151, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.disql_button.setFont(font)
        self.disql_button.setObjectName("get_data_button")


        
        #sql选择按钮
        self.sql_jb_button = QtWidgets.QPushButton(self.centralwidget)
        self.sql_jb_button.setGeometry(QtCore.QRect(500, 15, 151, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sql_jb_button.setFont(font)
        self.sql_jb_button.setObjectName("sql_jb")

        
        #密码选择按钮
        self.pass_excel_button = QtWidgets.QPushButton(self.centralwidget)
        self.pass_excel_button.setGeometry(QtCore.QRect(820, 15, 171, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_excel_button.setFont(font)
        self.pass_excel_button.setObjectName("pass_excel")

        # 日志标签
        self.log_rizhi = QtWidgets.QLabel(self.centralwidget)
        self.log_rizhi.setGeometry(QtCore.QRect(21, 410, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.log_rizhi.setFont(font)
        self.log_rizhi.setObjectName("log_rizhi")


        #####################  输入框   #########################
        #disql的输入框
        self.disql_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.disql_input.setGeometry(QtCore.QRect(20, 85, 341, 51))
        self.disql_input.setObjectName("disql_input")
        self.disql_input.setPlainText("D:/qax/dmdbms/bin/DIsql.exe")


        #sql脚本的输入框
        self.sqljb_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sqljb_input.setGeometry(QtCore.QRect(400, 85, 381, 51))
        self.sqljb_input.setObjectName("sqljb_input")
        self.sqljb_input.setPlainText("2.sql")


        #密码输入框
        self.pass_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(810, 85, 211, 51))
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setPlainText("passwd1.xlsx")
        #self.data1 = self.pass_input.toPlainText()  # 获取输入的数据


        #日志框
        # self.show_log = QtWidgets.QListView(self.centralwidget)
        # self.show_log.setGeometry(QtCore.QRect(110, 290, 921, 331))
        # self.show_log.setObjectName("show_log")
        self.show_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.show_log.setGeometry(QtCore.QRect(110, 290, 921, 331))
        self.show_log.setObjectName("textBrowser")

        #####################  按钮   #########################
        #连接测试的按钮
        self.Connection_test_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connection_test_Button.setGeometry(QtCore.QRect(30, 170, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Connection_test_Button.setFont(font)
        self.Connection_test_Button.setObjectName("Connection_test_Button")

        #获取数据的按钮
        self.get_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_data_button.setGeometry(QtCore.QRect(300, 170, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.get_data_button.setFont(font)
        self.get_data_button.setObjectName("get_data_button")
        
        #转utf8的按钮
        self.to_utf8_button = QtWidgets.QPushButton(self.centralwidget)
        self.to_utf8_button.setGeometry(QtCore.QRect(570, 170, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_utf8_button.setFont(font)
        self.to_utf8_button.setObjectName("to_utf8_button")
        
        #转excel的按钮
        self.to_excel_button = QtWidgets.QPushButton(self.centralwidget)
        self.to_excel_button.setGeometry(QtCore.QRect(840, 170, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.to_excel_button.setFont(font)
        self.to_excel_button.setObjectName("to_excel_button")
        #self.to_excel_button.clicked.connect(lambda:self.get_from_input(self.data1))

        #ok的按钮
        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(10, 570, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "达梦数据库基线工具_By_Garck"))
        self.disql_button.setText(_translate("MainWindow", "选择Disql"))
        self.sql_jb_button.setText(_translate("MainWindow", "选择sql脚本"))
        self.pass_excel_button.setText(_translate("MainWindow", "选择密码excel表"))
        self.Connection_test_Button.setText(_translate("MainWindow", "连接测试"))
        self.get_data_button.setText(_translate("MainWindow", "获取数据"))
        self.to_utf8_button.setText(_translate("MainWindow", "结果转utf-8"))
        self.to_excel_button.setText(_translate("MainWindow", "结果转Excel"))
        self.log_rizhi.setText(_translate("MainWindow", "日志："))
        self.ok_button.setText(_translate("MainWindow", "OK"))


