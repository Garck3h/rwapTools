# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QTextOption, QTextCursor



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #按钮1
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(140, 140, 111, 50))
        self.pushButton_1.setObjectName("pushButton_1")

        # 按钮2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 140, 111, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        #输入框1
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 40, 191, 61))
        self.lineEdit.setObjectName("lineEdit")

        # 输入框2
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 40, 261, 61))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # 日志框
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 190, 531, 221))
        self.textBrowser.setObjectName("textBrowser")

        #self.plainTextEdit.setWordWrapMode(QTextOption.WordWrap)
        #self.plainTextEdit.moveCursor(QTextCursor.End)
        #self.plainTextEdit.ensureCursorVisible()
        #self.plainTextEdit.setLineWrapMode(QtWidgets.QTextEdit.w)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton2"))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton1"))





















class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))


class ControlBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlBoard, self).__init__()
        self.setupUi(self)
        # 下面将输出重定向到textBrowser中

        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)


        #self.pushButton_2.clicked.connect(self.printABCD)  #按钮的信号
        self.pushButton_2.clicked.connect(lambda :Get_Data().printABC())


    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()



    def printABCD(self):

        print('Begin')
        print("aaaaaaaaaaaaaaaa")
        print("bbbbbbbbbbbbbbbb")
        print("cccccccccccccccc")
        print("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        print("End")



class Get_Data():
    def printABC(self):
        print('Begin')
        print("qweaaaaa")
        print("asdbbbbbbbb")
        print("zxcccccccc")




if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ControlBoard()
    # 调自定义的界面（即刚转换的.py对象）
    #Ui = ControlBoard()  # 这里也引用了一次rwap.rwap_gui.mainwindows.py文件的名字注意
    #Ui.setupUi(MainWindow)
    # 显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())

    # app = QApplication(sys.argv)
    # win = ControlBoard()
    # win.show()
    # sys.exit(app.exec_())
