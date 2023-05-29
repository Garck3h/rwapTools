from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
from PyQt5 import QtGui
#from pyqt5_plugins.examplebutton import QtWidgets
from PyQt5 import QtCore, QtWidgets


class Dmsql_uimian(QMainWindow):
    def dmsql_ui(self):
        self.dmsql_ui_Form = QtWidgets.QWidget()
        self.dmsql_ui_Form.setObjectName("dmsql_ui_Form")

        self.dmsql_disql_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_disql_button.setGeometry(QtCore.QRect(5, 30, 41, 31))  # 右，下，往右长，往下长
        self.dmsql_disql_button.setText("")
        self.dmsql_disql_button.setObjectName("dmsql_disql_button")
        self.dmsql_disql_button.setIcon(QtGui.QIcon(":/ico/disql.ico"))  # 设置ico图标
        self.dmsql_disql_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_disql_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_disql_button.setToolTip("选择DIsql")#提示


        self.dmsql_disql_line = QtWidgets.QLineEdit(self.dmsql_ui_Form)
        self.dmsql_disql_line.setGeometry(QtCore.QRect(60, 30, 211, 31))
        self.dmsql_disql_line.setObjectName("dmsql_disql_line")
        self.dmsql_disql_line.setText("D:/dmdbms/bin/DIsql.exe")

        self.dmsql_pass_line = QtWidgets.QLineEdit(self.dmsql_ui_Form)
        self.dmsql_pass_line.setGeometry(QtCore.QRect(60, 110, 211, 31))
        self.dmsql_pass_line.setObjectName("dmsql_pass_line")
        self.dmsql_pass_line.setText("passwd1.xlsx")
        self.dmsql_pass_line.setPlaceholderText("请选择密码excel文件")

        self.dmsql_pass_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_pass_button.setGeometry(QtCore.QRect(5, 110, 41, 31))
        self.dmsql_pass_button.setText("")
        self.dmsql_pass_button.setObjectName("dmsql_pass_button")
        self.dmsql_pass_button.setIcon(QtGui.QIcon(":/ico/passwd.ico"))  # 设置ico图标
        self.dmsql_pass_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_pass_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_pass_button.setToolTip("选择密码文件")  # 提示

        self.dmsql_sql_line = QtWidgets.QLineEdit(self.dmsql_ui_Form)
        self.dmsql_sql_line.setGeometry(QtCore.QRect(340, 30, 211, 31))
        self.dmsql_sql_line.setObjectName("dmsql_sql_line")
        self.dmsql_sql_line.setText("2.sql")
        self.dmsql_sql_line.setPlaceholderText("请选择SQL脚本文件")


        self.dmsql_sql_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_sql_button.setGeometry(QtCore.QRect(290, 30, 41, 31))
        self.dmsql_sql_button.setText("")
        self.dmsql_sql_button.setObjectName("dmsql_sql_button")
        self.dmsql_sql_button.setIcon(QtGui.QIcon(":/ico/sql.ico"))  # 设置ico图标
        self.dmsql_sql_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_sql_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_sql_button.setToolTip("选择SQL脚本")  # 提示

        self.dmsql_testc_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_testc_button.setGeometry(QtCore.QRect(290, 110, 41, 31))
        self.dmsql_testc_button.setText("")
        self.dmsql_testc_button.setObjectName("dmsql_testc_button")
        self.dmsql_testc_button.setIcon(QtGui.QIcon(":/ico/lianjie.ico"))  # 设置ico图标
        self.dmsql_testc_button.setIconSize(QSize(32, 32))  # 设置ico图标的大小
        self.dmsql_testc_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_testc_button.setToolTip("连接测试")  # 提示

        self.dmsql_getdata_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_getdata_button.setGeometry(QtCore.QRect(360, 110, 41, 31))
        self.dmsql_getdata_button.setText("")
        self.dmsql_getdata_button.setObjectName("dmsql_getdata_button")
        self.dmsql_getdata_button.setIcon(QtGui.QIcon(":/ico/getdata1.ico"))  # 设置ico图标
        self.dmsql_getdata_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_getdata_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_getdata_button.setToolTip("获取数据")  # 提示

        self.dmsql_to_utf8_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_to_utf8_button.setGeometry(QtCore.QRect(430, 110, 41, 31))
        self.dmsql_to_utf8_button.setText("")
        self.dmsql_to_utf8_button.setObjectName("dmsql_to_utf8_button")
        self.dmsql_to_utf8_button.setIcon(QtGui.QIcon(":/ico/toutf8.ico"))  # 设置ico图标
        self.dmsql_to_utf8_button.setIconSize(QSize(30, 30))  # 设置ico图标的大小
        self.dmsql_to_utf8_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_to_utf8_button.setToolTip("转utf8")  # 提示

        self.dmsql_to_excel_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_to_excel_button.setGeometry(QtCore.QRect(495, 110, 41, 31))
        self.dmsql_to_excel_button.setText("")
        self.dmsql_to_excel_button.setObjectName("dmsql_to_excel_button")
        self.dmsql_to_excel_button.setIcon(QtGui.QIcon(":/ico/excel.ico"))  # 设置ico图标
        self.dmsql_to_excel_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_to_excel_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_to_excel_button.setToolTip("导出excel")  # 提示

        self.dmsql_Disql_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_Disql_label.setGeometry(QtCore.QRect(5, 70, 41, 16))
        self.dmsql_Disql_label.setObjectName("dmsql_Disql_label")

        self.dmsql_SQL_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_SQL_label.setGeometry(QtCore.QRect(300, 70, 41, 16))
        self.dmsql_SQL_label.setObjectName("dmsql_SQL_label")

        self.dmsql_pass_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_pass_label.setGeometry(QtCore.QRect(5, 150, 41, 16))
        self.dmsql_pass_label.setObjectName("dmsql_pass_label")

        self.dmsql_testc_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_testc_label.setGeometry(QtCore.QRect(280, 150, 61, 20))
        self.dmsql_testc_label.setObjectName("dmsql_testc_label")

        self.dmsql_get_data_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_get_data_label.setGeometry(QtCore.QRect(354, 150, 61, 20))
        self.dmsql_get_data_label.setObjectName("dmsql_get_data_label")

        self.dmsql_utf8_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_utf8_label.setGeometry(QtCore.QRect(427, 150, 51, 20))
        self.dmsql_utf8_label.setObjectName("dmsql_utf8_label")

        self.dmsql_excel_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_excel_label.setGeometry(QtCore.QRect(487, 150, 71, 20))
        self.dmsql_excel_label.setObjectName("dmsql_excel_label")

        self.dmsql_textBrowser = QtWidgets.QTextBrowser(self.dmsql_ui_Form)
        self.dmsql_textBrowser.setGeometry(QtCore.QRect(60, 190, 508, 421))
        self.dmsql_textBrowser.setObjectName("dmsql_textBrowser")

        self.dmsql_log_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_log_label.setGeometry(QtCore.QRect(5, 370, 41, 31))
        self.dmsql_log_label.setObjectName("dmsql_log_label")

        self.dmsql_clean_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_clean_button.setGeometry(QtCore.QRect(5, 190, 41, 31))
        self.dmsql_clean_button.setText("")
        self.dmsql_clean_button.setObjectName("dmsql_clean_button")
        self.dmsql_clean_button.setIcon(QtGui.QIcon(":/ico/clean.ico"))  # 设置ico图标
        self.dmsql_clean_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_clean_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_clean_button.setToolTip("清除日志")  # 提示

        self.dmsql_ok_button = QtWidgets.QPushButton(self.dmsql_ui_Form)
        self.dmsql_ok_button.setGeometry(QtCore.QRect(5, 540, 41, 31))
        self.dmsql_ok_button.setText("")
        self.dmsql_ok_button.setObjectName("dmsql_ok_button")
        self.dmsql_ok_button.setIcon(QtGui.QIcon(":/ico/ok.ico"))  # 设置ico图标
        self.dmsql_ok_button.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.dmsql_ok_button.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.dmsql_ok_button.setToolTip("一键完成")  # 提示

        self.dmsql_clean_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_clean_label.setGeometry(QtCore.QRect(5, 230, 71, 30))
        self.dmsql_clean_label.setObjectName("dmsql_clean_label")

        self.dmsql_label = QtWidgets.QLabel(self.dmsql_ui_Form)
        self.dmsql_label.setGeometry(QtCore.QRect(302, 620, 280, 16))
        self.dmsql_label.setObjectName("dmsql_label")

        _translate = QtCore.QCoreApplication.translate
        self.dmsql_Disql_label.setText(_translate("MainWindow", "DIsql"))
        self.dmsql_SQL_label.setText(_translate("MainWindow", "SQL"))
        self.dmsql_pass_label.setText(_translate("MainWindow", "密码"))
        self.dmsql_testc_label.setText(_translate("MainWindow", "连接测试"))
        self.dmsql_get_data_label.setText(_translate("MainWindow", "获取数据"))
        self.dmsql_utf8_label.setText(_translate("MainWindow", "转utf8"))
        self.dmsql_excel_label.setText(_translate("MainWindow", "导出Excel"))
        self.dmsql_log_label.setText(_translate("MainWindow", "日志："))
        self.dmsql_clean_label.setText(_translate("MainWindow", "清空："))
        self.dmsql_label.setText(_translate("MainWindow", "达梦数据库基线工具V1.2 By Garck3h"))
        return self.dmsql_ui_Form



