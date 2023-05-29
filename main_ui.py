import sys

from PyQt5.QtWidgets import QStackedWidget, QApplication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QVBoxLayout)

import images
import Rsas_Function
import System_Function
import Dmsql_Function
import Other_Function



class Rwap_Main(Rsas_Function.Rsas_Function, System_Function.System_Function,Dmsql_Function.Dmsql_Function,Other_Function.Other_Function):
#class Rwap_Main(QMainWindow,other_Ui.Other_uimian):
    def __init__(self):
        super(Rwap_Main, self).__init__()
        #self.setupUi(self)

        #self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏标题  将界面设置为无框

        self.setAttribute(Qt.WA_TranslucentBackground) #将界面属性设置为半透明 这个是必须的
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window) # 隐藏标题  将界面设置为无框

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 290)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.toolbar_1(MainWindow)  #执行第一条Qtoolbar的函数
        self.toolbar_2(MainWindow)  # 执行第二条Qtoolbar的函数

        #创建一个QVBoxLayout
        self.Layout = QVBoxLayout(self.centralwidget)
        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)


        self.rsas_ui()   #实例化漏扫的页面
        self.system_ui()  # 操作系统
        self.dmsql_ui()  #达梦数据库的页面
        self.other_ui()#其它页面


        self.stackedWidget.addWidget(self.rsas_ui())  # 把这个漏扫页面添加到stackedWidget
        self.stackedWidget.addWidget(self.system_ui())  # 把这个操作系统页面添加到stackedWidget
        self.stackedWidget.addWidget(self.dmsql_ui())  # 把这个达梦数据库页面添加到stackedWidget
        self.stackedWidget.addWidget(self.other_ui())#把这个其它页面添加到stackedWidget


        #实现类 函数执行 Other_Function类中的Other_Impl
        self.rsas_Implement()       #漏扫的实现类
        self.system_Implement()     #操作系统的实现类
        self.dmsql_Implement()      #达梦的实现类
        self.Other_Implement()      #其它的实现类


        MainWindow.setCentralWidget(self.centralwidget)  # 原本的  设置中心窗口
        # self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def toolbar_1(self,MainWindow):
        toolBar = QtWidgets.QToolBar(self)  # 定义一个QToolBar
        #toolBar.setStyleSheet("QToolBar{spacing:-1px;}")
        MainWindow.addToolBar(Qt.TopToolBarArea, toolBar)  # 将这个toolbar置顶
        toolBar.setContextMenuPolicy(Qt.PreventContextMenu) #关闭右键 能关闭工具栏的操作
        toolBar.setMovable(False)  # 设置为不可移动，这样子灰色虚线就看不见了
        toolBar.setStyleSheet("QToolBar{border:none;spacing:8px;}")  # 去掉QToolBar的边框
        btn_Close = QtWidgets.QToolButton(self)  #创建一个按钮，命名为btn_Close
        #btn_Close.setText('') #   设置按钮的名字
        btn_Close.setIcon(QIcon(":/ico/colse.ico"))  # 设置ico图标
        btn_Close.setToolTip("关闭")#按钮的提示
        #btn_Close.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置图标后不显示文字，这个可以让图标和文字同时显示
        btn_Close.clicked.connect(lambda: self.close())#关闭

        btn_Narrow = QtWidgets.QToolButton(self) #创建一个按钮，命名为btn_Narrow
        btn_Narrow.setText('') #   设置按钮的名字
        btn_Narrow.setIcon(QIcon(":/ico/zuixiao.ico"))  # 设置ico图标
        btn_Narrow.setToolTip("最小化")  # 按钮的提示
        btn_Narrow.clicked.connect(lambda: self.showMinimized())  #最小化

        btn_Full = QtWidgets.QToolButton(self) #创建一个按钮，命名为btn_Full
        btn_Full.setText('') #   设置按钮的名字
        btn_Full.setIcon(QIcon(":/ico/full.ico"))  # 设置ico图标
        btn_Full.setToolTip("全屏")  # 按钮的提示
        #btn_Full.clicked.connect(lambda: self.showFullscreen())  #全屏

        toolBar.addWidget(btn_Close) #将就按钮放入到toolBar中
        toolBar.addWidget(btn_Narrow) #将就按钮放入到toolBar中
        toolBar.addWidget(btn_Full) #将就按钮放入到toolBar中


    def toolbar_2(self,MainWindow):
        MainWindow.addToolBarBreak()  # 相当于起一个换行符，添加一个Break（破裂; 间断; 或译为区域），这时，新添加的工具条将不再紧跟前一个工具条，而是另起一行。
        toolBar = QtWidgets.QToolBar(self)  # 定义一个QToolBar
        MainWindow.addToolBar(Qt.TopToolBarArea, toolBar)  # 将这个toolbar置顶
        toolBar.setMovable(False)  # 设置为不可移动，这样子灰色虚线就看不见了
        toolBar.setStyleSheet("QToolBar{border:none}")  # 去掉QToolBar的边框
        toolBar.setContextMenuPolicy(Qt.PreventContextMenu)  # 关闭右键 能关闭工具栏的操作
        self.label_Empty = QtWidgets.QLabel(self)  # 创建一个空白标签，命名为btn_Empty
        self.label_Empty.setText('            ')  # 设置按钮的名字

        self.btn_Rsas = QtWidgets.QToolButton(self)  # 创建一个按钮，命名为btn_Close
        self.btn_Rsas.setText('漏扫基线')  # 设置按钮的名字
        self.btn_Rsas.setIcon(QIcon(":/ico/rsas.ico"))  #设置ico图标
        self.btn_Rsas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) #设置图标后不显示文字，这个可以让图标和文字同时显示
        self.btn_Rsas.clicked.connect(lambda: self.onButtonClicked(0,MainWindow)) #创建一个信号，设置序号为0
        self.btn_Rsas.setCheckable(True)      #即设置后按钮想点灯开关一样，能够按一下保持一直开，再按下保持一直关
        self.btn_Rsas.setAutoExclusive(True)  #设置自动排它


        self.btn_System = QtWidgets.QToolButton(self)  # 创建一个按钮，命名为btn_Narrow
        self.btn_System.setText('操作系统')  # 设置按钮的名字
        self.btn_System.setIcon(QIcon(":/ico/System.ico"))  # 设置ico图标
        self.btn_System.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置图标后不显示文字，这个可以让图标和文字同时显示
        self.btn_System.clicked.connect(lambda: self.onButtonClicked(1,MainWindow)) #创建一个信号，设置序号为1
        self.btn_System.setCheckable(True)
        self.btn_System.setAutoExclusive(True)

        self.btn_Dmsql = QtWidgets.QToolButton(self)  # 创建一个按钮，命名为btn_Full
        self.btn_Dmsql.setText('达梦数据库')  # 设置按钮的名字
        self.btn_Dmsql.setIcon(QIcon(":/ico/dameng.ico"))  # 设置ico图标
        self.btn_Dmsql.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置图标后不显示文字，这个可以让图标和文字同时显示
        self.btn_Dmsql.clicked.connect(lambda: self.onButtonClicked(2, MainWindow))  # 创建一个信号，设置序号为2
        self.btn_Dmsql.setCheckable(True)
        self.btn_Dmsql.setAutoExclusive(True)

        self.btn_Other = QtWidgets.QToolButton(self)  # 创建一个按钮，命名为btn_Other
        self.btn_Other.setText('其它')  # 设置按钮的名字
        self.btn_Other.clicked.connect(lambda: self.onButtonClicked(3, MainWindow))  # 创建一个信号，设置序号为2
        self.btn_Other.setIcon(QIcon(":/ico/other.ico"))  # 设置ico图标
        self.btn_Other.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置图标后不显示文字，这个可以让图标和文字同时显示
        self.btn_Other.setCheckable(True)
        self.btn_Other.setAutoExclusive(True)

        toolBar.addWidget(self.label_Empty)  # 将空白标签放入到toolBar中
        toolBar.addWidget(self.btn_Rsas)  # 将按钮放入到toolBar中
        toolBar.addWidget(self.btn_System)  # 将按钮放入到toolBar中
        toolBar.addWidget(self.btn_Dmsql)  # 将按钮放入到toolBar中
        toolBar.addWidget(self.btn_Other)  # 将按钮放入到toolBar中



    def onButtonClicked(self, index,MainWindow):
        if index < self.stackedWidget.count():
            self.stackedWidget.setCurrentIndex(index)
            # 下面是自己添加的，改变页面大小的
            if index == 0:
                MainWindow.resize(529, 290)
                self.label_Empty.setText('            ')  # 设置空白标签的名字,减少工具栏第一个按钮的长度，恢复初始化


             #操作系统基线
            if index == 1:
                MainWindow.resize(529, 550)
                self.label_Empty.setText('            ')  # 设置空白标签的名字,减少工具栏第一个按钮的长度，恢复初始化

                # self.btn_Rsas.setCheckable(False)
                # self.btn_System.setCheckable(True)
                # self.btn_Dmsql.setCheckable(False)
                # self.btn_Other.setCheckable(False)
            if index == 2:
                MainWindow.resize(600, 755)
                self.label_Empty.setText('                 ')  # 设置空白标签的名字,增加工具栏第一个按钮的长度
                # self.btn_Rsas.setCheckable(False)
                # self.btn_System.setCheckable(False)
                # self.btn_Dmsql.setCheckable(True)
                # self.btn_Other.setCheckable(False)
            if index == 3:
                MainWindow.resize(529, 310)
                self.label_Empty.setText('            ')  # 设置空白标签的名字,减少工具栏第一个按钮的长度，恢复初始化
                # self.btn_Rsas.setCheckable(False)
                # self.btn_System.setCheckable(False)
                # self.btn_Dmsql.setCheckable(False)
                # self.btn_Other.setCheckable(True)



if __name__ == '__main__':

    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Rwap_Main()
    # 调自定义的界面（即刚转换的.py对象）
    #Ui = ControlBoard()  # 这里也引用了一次rwap.rwap_gui.mainwindows.py文件的名字注意
    #Ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("入网安评工具V2.6")
    MainWindow.setWindowIcon(QIcon(':/ico/logo.ico'))
    # 显示窗口并释放资源
    # 获取桌面属性
    desktop = QApplication.desktop()
    # 通过桌面的宽和高来比例位置显示,设置打开的时候默认的位置
    MainWindow.move(int(desktop.width() * 0.15), int(desktop.height() * 0.2))
    MainWindow.show()
    sys.exit(app.exec_())