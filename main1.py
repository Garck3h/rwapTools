#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PyQt5 import QtCore, QtGui
import sys
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui_ControlBoard import Ui_MainWindow


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

        self.pushButton.clicked.connect(self.printABCD)  #按钮的信号


    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    # def bClicked(self):
    #     """Runs the main function."""
    #     print('Begin')
    #
    #     self.printABCD()
    #
    #     print("End")

    def printABCD(self):
        print('Begin')
        print("aaaaaaaaaaaaaaaa")
        print("bbbbbbbbbbbbbbbb")
        print("cccccccccccccccc")
        print("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        print("End")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ControlBoard()
    win.show()
    sys.exit(app.exec_())


