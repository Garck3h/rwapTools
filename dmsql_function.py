from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from functools import partial
import sys
import dmsql_ui
import xlrd
import os
import pandas as pd
import numpy as np
import re
import chardet
import codecs
import getopt
import shutil
import sys
import subprocess

dir_name = 'data_sql'
oupt_name_sql_excel = 'sql_result.xlsx'
#disqlqw = 'D:/qax/dmdbms/bin/DIsql.exe'
#sqlqw = 'D:/qax/dmjx/2.sql'
#file_inputqw = 'E:/code/python_qt/rwapgui/passwd1.xlsx'


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))

class Show_Main(QMainWindow, dmsql_ui.Ui_MainWindow):
    def __init__(self):
        super(Show_Main, self).__init__()
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  #隐藏标题
        #self.setWindowFlags(Qt.FramelessWindowHint)  #隐藏标题




        # 下面将输出重定向到textBrowser中
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

       #选择disql的按钮
        self.disql_button.clicked.connect(lambda:self.load_disql())

       #选择sql脚本的按钮
        self.sql_jb_button.clicked.connect(lambda:self.load_sqljb())

       #选择密码表格的按钮
        self.pass_excel_button.clicked.connect(lambda:self.load_passwdf())

        #连接测试按钮
        self.Connection_test_Button.clicked.connect(lambda: lianjie_ceshi().read_get_Data(self.disql_input.toPlainText(), self.pass_input.toPlainText()))
        #self.Connection_test_Button.clicked.connect(lambda:lianjie_ceshi().read_get_Data(disqlqw,file_inputqw))

        #获取数据按钮
        #self.get_data_button.clicked.connect(lambda: self.Disql())
        self.get_data_button.clicked.connect(
            lambda: get_Data.read_get_Data(dir_name, self.disql_input.toPlainText(), self.sqljb_input.toPlainText(), self.pass_input.toPlainText()))
        #self.get_data_button.clicked.connect(lambda:disqlqw,sqlqw,file_inputqw)

        #转utf-8的按钮
        self.to_utf8_button.clicked.connect(lambda: gbkToUtf8.ReadDirectoryFile(dir_name))


        #转excel的按钮
        #self.to_excel_button.clicked.connect(lambda :Get_Data().printABC())
        #self.to_excel_button.clicked.connect(lambda: Get_Data().printAB())
        self.to_excel_button.clicked.connect(lambda:txtToExcel().txt_to_excel_run())

        #ok按钮，一键完成
        self.ok_button.clicked.connect(lambda: get_Data.read_get_Data(dir_name, self.disql_input.toPlainText(), self.sqljb_input.toPlainText(), self.pass_input.toPlainText()))
        self.ok_button.clicked.connect(lambda: gbkToUtf8.ReadDirectoryFile(dir_name))
        self.ok_button.clicked.connect(lambda:txtToExcel().txt_to_excel_run())



    #重写以下的三个方法可以让被隐藏图标后的界面可以移动
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



    def outputWritten(self, text): #输出内容在日志框架的函数
        cursor = self.show_log.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.show_log.setTextCursor(cursor)
        self.show_log.ensureCursorVisible()

    def load_disql(self):  #选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'exe文件(*.exe)')  # 返回选择文件的名字
        print("已选择Disql：",filenames)
        self.disql_input.setPlainText(filenames)

    def load_sqljb(self):  #选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'sql文件(*.sql)')  # 返回选择文件的名字
        print("sql脚本：",filenames)
        self.sqljb_input.setPlainText(filenames)

    def load_passwdf(self):  #选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'xlsx文件(*.xlsx *.xls)')  # 返回选择文件的名字
        print("已选择密码文件：",filenames)
        self.pass_input.setPlainText(filenames)


class lianjie_ceshi():
    @classmethod
    def TestConnection(self,command_test,ip,port):
        try:
            subp = subprocess.Popen(command_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                print(ip,":",port," ----- Connection Success!!")
                #lianjie_ceshi().cmd(command,ip,port)
            else:
                print("连接失败")
        except Exception as e:
            # print(e)
            print(ip,":",port," ----- Connection Failed, User name or password error!!")


    @classmethod
    def cmd(self,command,ip,port):
        try:
            subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                print(ip,":",port," ----- Get data Success!!")

            else:
                print("失败")
        except Exception as e:
            # print(e)
            print(ip,":",port," -----")


    @classmethod
    def read_get_Data(self,input_disql,input_file):
        print("\n")
        print("连接情况：")
        disql = input_disql
        input_file = input_file
        try:
            # 打开excle表格，参数是文件路径
            a = xlrd.open_workbook(input_file)
            table = a.sheet_by_name("Sheet1")  # 通过表格的名称获取

            # 获取列的数据，colx第一列，start_rowx从第二个值开始
            ip_adress = table.col_values(colx=0, start_rowx=1, end_rowx=None)
            username = table.col_values(colx=1, start_rowx=1, end_rowx=None)
            passwd = table.col_values(colx=2, start_rowx=1, end_rowx=None)
            port1 = table.col_values(colx=3, start_rowx=1, end_rowx=None)
            port = []

            for i in range(len(port1)):
                port.append(int(port1[i]))
            print(ip_adress)
            print(username)
            #print(passwd)
            print(port)

            #comd = disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c"+" " + "exit"
            #print(comd)
            for i in range(len(ip_adress)):
                #print(comd)
                lianjie_ceshi().TestConnection(disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c"+" " + "exit",ip_adress[i],port[i])
        except:
            print("----- Error, no password file found！！")



class get_Data():
    @classmethod
    def TestConnection(self,command_test,command,ip,port):
        try:
            subp = subprocess.Popen(command_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                print(ip,":",port," ----- Connection Success!!")
                get_Data.cmd(command,ip,port)
            else:
                print("连接失败")
        except Exception as e:
            # print(e)
            print(ip,":",port," ----- Connection Failed, User name or password error!!")


    @classmethod
    def cmd(self,command,ip,port):
        try:
            subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                print(ip,":",port," ----- Get data Success!!")
                # print(subp.communicate()[1])
            else:
                print("Get failed!!!")
        except Exception as e:
            # print(e)
            print(ip,":",port," error  ----- Get data failed!!!  Please check the sql script entered！")


    @classmethod
    def read_get_Data(self,input_dir_name,input_disql,input_sql,input_file):
        print("\n")
        print("获取情况：")
        dir_name = input_dir_name
        disql = input_disql
        sql = input_sql
        input_file = input_file
        #print(dir_name,disql,sql,input_file)

        if os.path.exists(dir_name): #如果存在data_sql就先删除，以确保数据是最新的，而不是在原来的基础上添加的
            shutil.rmtree(dir_name)
        if not os.path.isdir(dir_name):  # 如果没有文件夹data_sql，就会自己创建一个
            os.makedirs(dir_name)



        try:
            # 打开excle表格，参数是文件路径
            a = xlrd.open_workbook(input_file)
            table = a.sheet_by_name("Sheet1")  # 通过表格的名称获取

            # 获取列的数据，colx第一列，start_rowx从第二个值开始
            ip_adress = table.col_values(colx=0, start_rowx=1, end_rowx=None)
            username = table.col_values(colx=1, start_rowx=1, end_rowx=None)
            passwd = table.col_values(colx=2, start_rowx=1, end_rowx=None)
            port1 = table.col_values(colx=3, start_rowx=1, end_rowx=None)
            port = []

            for i in range(len(port1)):
                port.append(int(port1[i]))
            print(ip_adress)
            print(username)
            #print(passwd)
            print(port)

            for i in range(len(ip_adress)):
                get_Data.TestConnection(disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c exit",disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " " + "`" +sql
                             + ">>" + "./" + dir_name + "/" + ip_adress[i] + "-" + str(port[i]) + ".txt",ip_adress[i],port[i])
        except:
            print("----- Error, no password file found！！")



class gbkToUtf8():  #转utf-8的类
    @classmethod
    def WriteFile(self,filePath, u, encoding="utf-8"):
        with codecs.open(filePath, "w", encoding) as f:
            f.write(u)

    @classmethod
    def GBK_2_UTF8(self,src, dst):
        #     检测编码，coding可能检测不到编码，有异常
        f = open(src, "rb")
        coding = chardet.detect(f.read())["encoding"]
        f.close()
        if coding != "utf-8":
            with codecs.open(src, "r", coding) as f:
                try:
                    gbkToUtf8.WriteFile(dst, f.read(), encoding="utf-8")
                    try:
                        print(src + "  " + coding + " to utf-8  converted!")
                    except Exception:
                        print("print error")
                except Exception:
                    print(src + "  " + coding + "  read error")

    # 把目录中的*.txt编码由gbk转换为utf-8
    @classmethod
    def ReadDirectoryFile(self,rootdir):
        print("\n")
        print("转换情况：")
        try:
            for parent, dirnames, filenames in os.walk(rootdir):
                for dirname in dirnames:
                    # 递归函数，遍历所有子文件夹
                    gbkToUtf8.ReadDirectoryFile(dirname)
                for filename in filenames:
                    if filename.endswith(".txt"):
                        gbkToUtf8.GBK_2_UTF8(os.path.join(parent, filename),
                                   os.path.join(parent, filename))
            print("全部文件转换utf-8 成功！")
        except:
            print("读取的数据不是gbk编码，请重新获取数据！！")




#txt文件转成excel的类
class txtToExcel():
    @classmethod
    def transformation(self,file_name_src_hanshu):  # 读取数据、转换格式，转成一维数组，然后在每个元素的中间都加上换行符
        try:
            data = pd.read_table(file_name_src_hanshu, header=None, delimiter="\t")  # 读取txt的内容
            data1 = data.to_numpy()  # 将pd格式转成数组格式
            data2 = list(np.array(data1).flatten())  # 二维数组转成一维数组
            # 在数组的元素之间添加换行符号
            # flgei = 1
            # while flgei < len(data2):
            #     data2.insert(flgei, '\n')
            #     flgei += 2
            return data2
        except:
            print("未找到文件！！")
            print("请先删除本目录下的data文件夹！！！")

    @classmethod
    def flag_bit(self,data2_hanshu):  # 获取标志位
        data2 = data2_hanshu
        flag_nu = []
        # print(flag_nu)
        for x in range(len(data2)):
            target_str = re.match("SQL>", data2[x])  # 定义个变量，使用正则去匹配有没有特定值的，如果有就返回一个匹配的对象，没有就返回None
            if target_str != None:  # if判断是否有
                flag_nu.append(x)
        flag_nu.append(len(data2))
        del (flag_nu[-1])
        return flag_nu

    @classmethod
    def merge_hebing(self,flag_nu_hanshu, data2_hanshu):
        flag_nu = flag_nu_hanshu
        data2 = data2_hanshu
        end_data = []
        for x in range(len(flag_nu) - 1):
            end_data.append(
                '\n'.join(data2[slice(flag_nu[x], flag_nu[x + 1], 1)]))  # 根据位置截取数组中的内容合并为一个元素，然后一一添加到end_dataq数组中
        return end_data

    @classmethod
    def txt_to_excel_run(self):
        src_path = dir_name + '/'
        ip_address_and_port = []  # 用于存储ip地址
        end_data_huizong = []  # 用于将所有的内容存在到里面，形成了一个二维数组，每个元素对应一个数组，即IP的内容，
        geshu = 0
        print("\n")
        print("result:")
        try:
            for root, dirs, files in os.walk(src_path):
                for i in files:
                    file_name_src = src_path + i
                    ip = file_name_src.replace(src_path, '').replace('.txt', '').replace('-', ':')
                    print(ip, "  Success!")
                    geshu = geshu + 1
                    ip_address_and_port.append(ip)

                    # print("第一个函数：",txtToExcel.transformation(file_name_src))
                    # print("第二个函数：",txtToExcel.flag_bit(txtToExcel.transformation(file_name_src)) )
                    # print("第三个函数：",merge_hebing(flag_bit(transformation(file_name_src)),transformation(file_name_src)))

                    end_data_huizong.append(self.merge_hebing(self.flag_bit(self.transformation(file_name_src)),self.transformation(file_name_src)))
            # 将IP和全部数据的二维数组构造成一个字典
            zidian = dict(zip(ip_address_and_port, end_data_huizong))
            # print(zidian)
            df = pd.DataFrame(zidian)
            df.to_excel(oupt_name_sql_excel, '安全通用要求-操作系统安全', index=False)
            print("\n" + "共完成了", geshu, "个数据库的合并")
            print("请查看：" + oupt_name_sql_excel )
        except:
            print("读取的文件格式有误！！")



if __name__ == '__main__':
    #获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Show_Main()
    # 调自定义的界面（即刚转换的.py对象）
    #Ui = ControlBoard()  # 这里也引用了一次rwap.rwap_gui.mainwindows.py文件的名字注意
    #Ui.setupUi(MainWindow)
    # 显示窗口并释放资源
    MainWindow.show()
    sys.exit(app.exec_())
