import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets


import main_ui
from PyQt5.QtCore import Qt


class Show_Main(main_ui.Rwap_Main):
    def __init__(self):
        super(Show_Main, self).__init__()
        self.setupUi(self)#调用显示的类

        #添加阴影
        self.shadow = QGraphicsDropShadowEffect()  # 设定一个阴影,半径为10,颜色为#444444,定位为0,0
        self.shadow.setBlurRadius(10) #
        self.shadow.setColor(QColor("#444444")) #
        self.shadow.setOffset(0, 0) #
        self.setGraphicsEffect(self.shadow)#给当前对象  设定阴影效果

    # 重写以下的三个方法可以让被隐藏图标后的界面可以移动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def paintEvent(self, event):
        # 圆角
        pat2 = QPainter(self)
        pat2.setRenderHint(pat2.Antialiasing)  # 抗锯齿
        pat2.setBrush(Qt.white)
        pat2.setPen(Qt.transparent)

        rect = self.rect()
        rect.setLeft(5)
        rect.setTop(5)
        rect.setWidth(rect.width() - 5)
        rect.setHeight(rect.height() - 5)
        pat2.drawRoundedRect(rect, 8, 8)



if __name__ == '__main__':

    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Show_Main()
    # 调自定义的界面（即刚转换的.py对象）
    #Ui = ControlBoard()  # 这里也引用了一次rwap.rwap_gui.mainwindows.py文件的名字注意
    #Ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("入网安评工具V2.6")
    MainWindow.setWindowIcon(QIcon(':/ico/logo.ico'))
    # 显示窗口并释放资源
    # 获取桌面属性
    desktop = QApplication.desktop()
    # 通过桌面的宽和高来比例位置显示,设置打开的时候默认的位置
    MainWindow.move(int(desktop.width() * 0.18), int(desktop.height() * 0.28))
    MainWindow.show()
    sys.exit(app.exec_())
