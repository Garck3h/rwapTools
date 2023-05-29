"""
文件对话框: QFileDialog
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本对话框演示")
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        # 绑定加载图片的功能
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        #绑定加载文本的功能
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)


    def loadImage(self):
        #打开对话框, "打开文件"(对话框的名字), '.'(打开当前的路径), '图像文件(*.jpg *.png)'(打开文件的格式)
        fname, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')

        self.imageLabel.setPixmap(QPixmap(fname)) # 根据路径, 设置对应的图片


    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile) #设置能打开文件的格式
        dialog.setFilter(QDir.Files) #设置为当前的路径


        if dialog.exec():
            filenames = dialog.selectedFiles() #返回选择文件的名字
            print(filenames)  #路径的地址
            # 打开文件, 将里面的文本显示在文本框中
            f = open(filenames[0], "r", encoding='utf-8')
            with f:
                data = f.read() #一次性读取所有文件内容
                self.contents.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = QFileDialogDemo()
    main.show()

    sys.exit(app.exec_())