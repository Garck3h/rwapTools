#coding=utf-8
import sys

from PyQt5.QtWidgets import QMainWindow


from PyQt5 import QtCore, QtGui, QtWidgets
import dmsql_ui
import system_ui
import mainwindows
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *




if __name__ == '__main__':
    # 获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 调自定义的界面（即刚转换的.py对象）
    Ui = mainwindows.Ui_MainWindow()  # 这里也引用了一次rwap.rwap_gui.mainwindows.py文件的名字注意
    Ui.setupUi(MainWindow)
    # 显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
