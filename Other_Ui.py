from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic.properties import QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5 import  QtGui
from PyQt5 import QtCore, QtWidgets


class Other_uimian(QMainWindow):
    def other_ui(self):
        self.other_ui_Form = QtWidgets.QWidget()  # 创建一个页面，命名为rsas_ui_Form
        self.other_ui_Form.setObjectName("rsas_ui_Form")  # 使用setObjectName方法让子控件动态改变qss样式

        self.other_filedir_btn = QtWidgets.QPushButton(self.other_ui_Form)
        self.other_filedir_btn.setGeometry(QtCore.QRect(30, 50, 51, 31))  # 右，下，往右长，往下长
        self.other_filedir_btn.setObjectName("self.other_filedir_btn")  # 使用setObjectName方法让子控件动态改变qss样式
        self.other_filedir_btn.setIcon(QtGui.QIcon(":/ico/dirs.ico"))  # 设置ico图标
        self.other_filedir_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.other_filedir_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.other_filedir_btn.setToolTip("选择文件夹")

        self.other_rule_label = QtWidgets.QLabel(self.other_ui_Form)
        self.other_rule_label.setGeometry(QtCore.QRect(40, 100, 51, 31))
        self.other_rule_label.setObjectName("self.other_rule_label")
        self.other_rule_label.setText(QtCore.QCoreApplication.translate("MainWindow", "规则："))


        self.other_lineEdit_dir = QtWidgets.QLineEdit(self.other_ui_Form)
        self.other_lineEdit_dir.setGeometry(QtCore.QRect(120, 50, 310, 32))
        self.other_lineEdit_dir.setObjectName("self.other_lineEdit_dir")
        self.other_lineEdit_dir.setPlaceholderText("请选择文件夹")

        self.other_lineEdit_rule = QtWidgets.QLineEdit(self.other_ui_Form)
        self.other_lineEdit_rule.setGeometry(QtCore.QRect(120, 100, 310, 32))
        self.other_lineEdit_rule.setObjectName("self.other_lineEdit_rule")
        self.other_lineEdit_rule.setPlaceholderText("请输入匹配规则")


        self.other_start_btn = QtWidgets.QPushButton(self.other_ui_Form)
        self.other_start_btn.setGeometry(QtCore.QRect(30, 140, 51, 31))
        self.other_start_btn.setObjectName("self.other_start_btn")
        self.other_start_btn.setIcon(QtGui.QIcon(":/ico/start.ico"))  # 设置ico图标
        self.other_start_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.other_start_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.other_start_btn.setToolTip("开始")

        #self.stackedWidget.addWidget(self.rsas_ui_Form  )  # 把这个页面放入到stackedWidget
        return self.other_ui_Form


