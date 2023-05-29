
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import  QFileDialog, QApplication
import xlrd
import os
import pandas as pd
import numpy as np
import re
import chardet
import codecs
import shutil
import sys
import subprocess
import Dmsql_Ui



dir_name = './data_sql'
oupt_name_sql_excel = 'sql_result.xlsx'


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号  #pyqtSignal声明无参数信号
    #textWritten = QtCore.
    def write(self, text):
        self.textWritten.emit(str(text))
        loop = QEventLoop()
        QTimer.singleShot(1, loop.quit)
        loop.exec()
        QApplication.processEvents()  #实时刷新界面
        #self.textWritten.emit(str(text))


class Dmsql_Function(Dmsql_Ui.Dmsql_uimian):

    def __init__(self):
        super(Dmsql_Function, self).__init__()



    def stdout_on(self):  # 开启打印在日志框
        self.stdout_temp = sys.stdout  # 暂存，用于下面的恢复
        sys.stdout = EmittingStr()  #打印输出
        sys.stdout.textWritten.connect(self.outputWritten)
        sys.stdout = sys.stdout
        sys.stderr = EmittingStr()  #打印错误
        sys.stderr.textWritten.connect(self.outputWritten)


    def stdout_off(self): # 关闭打印在日志框
        sys.stdout = self.stdout_temp #打印输出
        sys.stderr = self.stdout_temp  #打印错误

    #重新定义一个打印的时候没有输出在日志框的函数
    def printt(self,input):
        self.stdout_off()  # 关闭打印在日志框
        print(input)
        self.stdout_on()  # 开启打印在日志框

    def dmsql_Implement(self):
        self.stdout_on() #开启打印在日志框
        print("Welcome to Damon Database Baseline Tool!")
        #self.stdout_off()#关闭打印在日志框

        # 选择disql的按钮
        self.dmsql_disql_button.clicked.connect(lambda: self.load_disql())
        # 选择sql脚本的按钮
        self.dmsql_sql_button.clicked.connect(lambda: self.load_sqljb())
        # 选择密码表格的按钮
        self.dmsql_pass_button.clicked.connect(lambda: self.load_passwdf())

        #连接测试按钮
        self.dmsql_testc_button.clicked.connect(lambda: lianjie_ceshi().read_get_Data(self.dmsql_disql_line.text(), self.dmsql_pass_line.text()))
        # 获取数据按钮
        self.dmsql_getdata_button.clicked.connect(
            lambda: get_Data.read_get_Data(dir_name, self.dmsql_disql_line.text(), self.dmsql_sql_line.text(),self.dmsql_pass_line.text()))
        # 转utf-8的按钮
        self.dmsql_to_utf8_button.clicked.connect(lambda: gbkToUtf8.ReadDirectoryFile(dir_name))
        # 转excel的按钮
        self.dmsql_to_excel_button.clicked.connect(lambda: txtToExcel().txt_to_excel_run())

        # ok按钮，一键完成
        self.dmsql_ok_button.clicked.connect(
            lambda: get_Data.read_get_Data(dir_name, self.dmsql_disql_line.text(), self.dmsql_sql_line.text(),self.dmsql_pass_line.text()))
        self.dmsql_ok_button.clicked.connect(lambda: gbkToUtf8.ReadDirectoryFile(dir_name))
        self.dmsql_ok_button.clicked.connect(lambda: txtToExcel().txt_to_excel_run())

        #清空按钮
        self.dmsql_clean_button.clicked.connect(lambda: self.dmsql_textBrowser.setText(""))



    def outputWritten(self, text):  # 输出内容在日志框架的函数
        cursor = self.dmsql_textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.dmsql_textBrowser.setTextCursor(cursor)  #更新可见光标
        self.dmsql_textBrowser.ensureCursorVisible()  # 这种方法会在添加文本后 自动换行

    def load_disql(self):  # 选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'exe文件(*.exe)')  # 返回选择文件的名字
        if filenames:
            self.dmsql_disql_line.setText(filenames)
            print("\n选择Disql：", filenames)


    def load_sqljb(self):  # 选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'sql文件(*.sql)')  # 返回选择文件的名字
        if filenames:
            self.dmsql_sql_line.setText(filenames)
            print("\nsql脚本：", filenames)

    def load_passwdf(self):  # 选择disql文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'xlsx文件(*.xlsx *.xls)')  # 返回选择文件的名字
        if filenames:
            self.dmsql_pass_line.setText(filenames)
            print("\n选择密码文件：", filenames)





class lianjie_ceshi():
    @classmethod
    def TestConnection(self,command_test,ip,port):
        try:
            subp = subprocess.Popen(command_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                print(ip,":",port," ----- Connection Success!!")
                #lianjie_ceshi().cmd(command_test,ip,port)
            else:
                print("连接失败")
            #os.killpg(subp.pid, signal.SIGTERM)
        except Exception as e:
            # print(e)
            print(ip,":",port," ----- Connection Failed, User name or password error!!")

    @classmethod
    def read_get_Data(self,input_disql,input_file):
        print("\n")
        print("连接情况：")
        disql = input_disql
        input_file = input_file
        #判断disql文件是否存在
        if(os.path.exists(disql)):
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
                    lianjie_ceshi().TestConnection(disql + " " + "\"\"\"" + username[i] + "\"\"\"" + "/" + "\"\"\"" + passwd[i] + "\"\"\"" + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c"+" " + "exit",ip_adress[i],port[i])
                     #添加上三个双引号，为了避免密码中含有特殊字符（@、#等）引起的报错
            except:
                print("----- Error, no password file found！！")
        else:
            print("所选中的disql文件不存在")




class get_Data():
    @classmethod
    def TestConnection(self,command_test,command,ip,port):
        try:
            subp = subprocess.Popen(command_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding="utf-8")
            subp.wait(2)
            if subp.poll() == 0:
                #print(ip,":",port," ----- Connection Success!!")
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
                get_Data.TestConnection(disql + " " + "\"\"\"" + username[i] + "\"\"\"" + "/" + "\"\"\"" + passwd[i] + "\"\"\"" + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c exit",disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " " + "`" +sql
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
            #df = pd.DataFrame(zidian)
            df = pd.DataFrame(pd.DataFrame.from_dict(zidian, orient='index').values.T, columns=list(zidian.keys())) #防止输入的数值长度不一样的时候会崩掉
            df.to_excel(oupt_name_sql_excel, '安全通用要求-操作系统安全', index=False)
            print("\n" + "共完成了", geshu, "个数据库的合并")
            print("请查看：" + oupt_name_sql_excel )
        except:
            print("读取的文件格式有误！！")


