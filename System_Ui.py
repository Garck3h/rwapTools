from PyQt5.uic.properties import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
from PyQt5 import  QtGui
#from pyqt5_plugins.examplebutton import QtWidgets
from PyQt5 import QtCore, QtWidgets



class System_uimian(QMainWindow):
    def system_ui(self):
        self.system_ui_Form = QtWidgets.QWidget()  # 创建一个页面，命名为rsas_ui_Form
        self.system_ui_Form.setObjectName("system_ui_Form")  # 使用setObjectName方法让子控件动态改变qss样式

        #批量执行基线
        self.BatchBaselineLabel = QtWidgets.QLabel(self.system_ui_Form)
        self.BatchBaselineLabel.setGeometry(QtCore.QRect(10, 30, 172, 15))
        self.BatchBaselineLabel.setObjectName("label")
        self.BatchBaselineLabel.setText("批量执行基线：")

        # 选中资产按钮
        self.Baseline_file_btn = QtWidgets.QPushButton(self.system_ui_Form)
        self.Baseline_file_btn.setGeometry(QtCore.QRect(30, 80, 51, 31))  # 右，下，往右长，往下长
        self.Baseline_file_btn.setObjectName("system_file_btn")  # 使用setObjectName方法让子控件动态改变qss样式
        self.Baseline_file_btn.setIcon(QtGui.QIcon(":/ico/dirs.ico"))  # 设置ico图标
        self.Baseline_file_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.Baseline_file_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}"  # 鼠标经过的时候会有一个浅蓝色的轮廓
                                           "QPushButton{border:none}"  ## 取消按钮的轮廓
                                           )
        self.Baseline_file_btn.setToolTip("选择资产")

        # 输入框
        self.Baseline_lineEdit = QtWidgets.QLineEdit(self.system_ui_Form)
        self.Baseline_lineEdit.setGeometry(QtCore.QRect(120, 80, 331, 31))
        self.Baseline_lineEdit.setObjectName("Baseline_lineEdit")
        self.Baseline_lineEdit.setText("property.xlsx")
        self.Baseline_lineEdit.setPlaceholderText("请选择资产表格")

        self.Baseline_level = QtWidgets.QComboBox(self.system_ui_Form)
        self.Baseline_level.setGeometry(QtCore.QRect(120, 140, 100, 31))
        self.Baseline_level.setObjectName("Baseline_level")
        self.Baseline_level.addItems(['等保二级', '等保三级'])

        # 开始按钮
        self.Baseline_Start_Btn = QtWidgets.QPushButton(self.system_ui_Form)
        self.Baseline_Start_Btn.setGeometry(QtCore.QRect(30, 140, 51, 31))
        self.Baseline_Start_Btn.setText("")
        self.Baseline_Start_Btn.setObjectName("Baseline_Start_Btn")
        self.Baseline_Start_Btn.setIcon(QtGui.QIcon(":/ico/start.ico"))  # 设置ico图标
        self.Baseline_Start_Btn.setIconSize(QSize(30, 30))  # 设置ico图标的大小
        self.Baseline_Start_Btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}"  # 鼠标经过的时候会有一个浅蓝色的轮廓
                                            "QPushButton{border:none}"  ## 取消按钮的轮廓
                                            )
        self.Baseline_Start_Btn.setToolTip("开始批量检查")



        #基线结果整理
        self.BatchBaselineLabel = QtWidgets.QLabel(self.system_ui_Form)
        self.BatchBaselineLabel.setGeometry(QtCore.QRect(10, 230, 172, 15))
        self.BatchBaselineLabel.setObjectName("label")
        self.BatchBaselineLabel.setText("基线结果整理：")

        #选中文件夹按钮
        self.system_file_btn = QtWidgets.QPushButton(self.system_ui_Form)
        self.system_file_btn.setGeometry(QtCore.QRect(30, 280, 51, 31))  # 右，下，往右长，往下长
        self.system_file_btn.setObjectName("system_file_btn")  # 使用setObjectName方法让子控件动态改变qss样式
        self.system_file_btn.setIcon(QtGui.QIcon(":/ico/dirs.ico"))  # 设置ico图标
        self.system_file_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.system_file_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.system_file_btn.setToolTip("选择文件夹")

        #输入框
        self.system_lineEdit = QtWidgets.QLineEdit(self.system_ui_Form)
        self.system_lineEdit.setGeometry(QtCore.QRect(120, 280, 331, 31))
        self.system_lineEdit.setObjectName("system_lineEdit")
        self.system_lineEdit.setPlaceholderText("请选择文件夹")

        #重命名按钮
        self.system_rename_btn = QtWidgets.QPushButton(self.system_ui_Form)
        self.system_rename_btn.setGeometry(QtCore.QRect(30, 360, 51, 31))
        self.system_rename_btn.setObjectName("system_rename_btn")
        self.system_rename_btn.setIcon(QtGui.QIcon(":/ico/rename.ico"))  # 设置ico图标
        self.system_rename_btn.setIconSize(QSize(36, 36))  # 设置ico图标的大小
        self.system_rename_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.system_rename_btn.setToolTip("批量重命名")

        #整理结果按钮
        self.system_start_btn = QtWidgets.QPushButton(self.system_ui_Form)
        self.system_start_btn.setGeometry(QtCore.QRect(120, 360, 51, 31))
        self.system_start_btn.setText("")
        self.system_start_btn.setObjectName("system_start_btn")
        self.system_start_btn.setIcon(QtGui.QIcon(":/ico/start.ico"))  # 设置ico图标
        self.system_start_btn.setIconSize(QSize(30, 30))  # 设置ico图标的大小
        self.system_start_btn.setStyleSheet("QPushButton:hover{background-color:rgba(229,243,255)}" #鼠标经过的时候会有一个浅蓝色的轮廓
                                         "QPushButton{border:none}"  ## 取消按钮的轮廓
                                         )
        self.system_start_btn.setToolTip("开始合并")
        #self.stackedWidget.addWidget(self.rsas_ui_Form  )  # 把这个页面放入到stackedWidget

        self.AuthorlineLabel = QtWidgets.QLabel(self.system_ui_Form)
        self.AuthorlineLabel.setGeometry(QtCore.QRect(310, 420, 200, 15))
        self.AuthorlineLabel.setObjectName("label")
        self.AuthorlineLabel.setText("基线工具V1.6 by Garck3h")


        return self.system_ui_Form


