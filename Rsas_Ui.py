from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
from PyQt5 import  QtGui
#from pyqt5_plugins.examplebutton import QtWidgets
from PyQt5 import QtCore, QtWidgets
#from pyqt5_plugins.examplebutton import QtWidgets

class Rsas_uimian(QMainWindow):
    def rsas_ui(self):
        self.rsas_ui_Form = QtWidgets.QWidget()  # 创建一个页面，命名为rsas_ui_Form
        self.rsas_ui_Form.setObjectName("rsas_ui_Form")  # 使用setObjectName方法让子控件动态改变qss样式

        self.rsas_file_btn = QtWidgets.QPushButton(self.rsas_ui_Form)  # 创建一个按钮，添加到rsas_ui_Form页面
        self.rsas_file_btn.setGeometry(QtCore.QRect(30, 50, 51, 31))  # 右，下，往右长，往下长
        self.rsas_file_btn.setObjectName("pushButton")  # 使用setObjectName方法让子控件动态改变qss样式
        self.rsas_file_btn.setIcon(QtGui.QIcon(":/ico/dirs.ico"))  # 设置ico图标
        self.rsas_file_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        #self.rsas_file_btn.setStyleSheet("border:none")  # 取消按钮的轮廓
        self.rsas_file_btn.setToolTip("选择文件夹")
        self.rsas_file_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )



        self.rsas_lineEdit = QtWidgets.QLineEdit(self.rsas_ui_Form)
        self.rsas_lineEdit.setGeometry(QtCore.QRect(120, 50, 300, 31))
        self.rsas_lineEdit.setObjectName("lineEdit")
        self.rsas_lineEdit.setPlaceholderText("请选择文件夹")

        self.rsas_QComboBox_rules = QtWidgets.QComboBox(self.rsas_ui_Form)
        self.rsas_QComboBox_rules.setGeometry(QtCore.QRect(120, 100, 100, 31))
        self.rsas_QComboBox_rules.setObjectName("rsas_QComboBox_rules")
        self.rsas_QComboBox_rules.addItems(['漏洞信息', '远程漏洞'])

        self.rsas_start_btn = QtWidgets.QPushButton(self.rsas_ui_Form)
        self.rsas_start_btn.setGeometry(QtCore.QRect(30, 130, 51, 31))
        self.rsas_start_btn.setObjectName("pushButton_2")
        self.rsas_start_btn.setIcon(QtGui.QIcon(":/ico/start.ico"))  # 设置ico图标
        self.rsas_start_btn.setIconSize(QSize(30, 30))  # 设置ico图标的大小
        self.rsas_start_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )  # 取消按钮的轮廓
        self.rsas_start_btn.setToolTip("开始合并")
        # self.stackedWidget.addWidget(self.rsas_ui_Form  )  # 把这个页面放入到stackedWidget
        return self.rsas_ui_Form



