# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 326)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81,187,98);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #路径显示框
        self.file_dir_show = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.file_dir_show.setGeometry(QtCore.QRect(140, 120, 431, 41))
        self.file_dir_show.setObjectName("file_dir_show")
        self.file_dir_show.setPlainText("rsas_src")



        #标题
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setObjectName("title")

        #文件路径选择按钮
        self.file_dir = QtWidgets.QPushButton(self.centralwidget)
        self.file_dir.setGeometry(QtCore.QRect(20, 120, 91, 41))
        self.file_dir.setObjectName("file_dir")

        #开始按钮
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 210, 91, 41))
        self.start.setObjectName("start")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSAS扫描结果整理工具_By_Garck"))
        self.file_dir.setText(_translate("MainWindow", "选择文件夹"))
        self.title.setText(_translate("MainWindow", "RSAS漏扫结果Excel整合"))
        self.start.setText(_translate("MainWindow", "开始"))
