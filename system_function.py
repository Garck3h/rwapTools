from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from functools import partial
import sys
import system_ui
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


class Show_Main(QMainWindow, system_ui.Ui_MainWindow):
    def __init__(self):
        super(Show_Main, self).__init__()
        self.setupUi(self)

        #选择文件夹
        #self.Connection_test_Button.clicked.connect(lambda: )
        self.xuanze_file_dir.clicked.connect(lambda: self.loadDir())
        #self.xuanze_file_dir.clicked.connect(lambda: QMessageBox.about(self, "提示", "我被点击了，哈哈哈哈"))

        #批量重命名
        self.rename.clicked.connect(lambda: renamefile().renamef(self.file_dir_show.toPlainText()))
        self.rename.clicked.connect(lambda:self.file_dir_show.setPlainText(outputdir.replace('/', '')))

        #txt转excel的按钮
        self.txt_to_excel.clicked.connect(lambda: txtToExcel().txt_to_excel_run(self.file_dir_show.toPlainText()))



    def loadDir(self):
        filenames = QFileDialog.getExistingDirectory(None, "选择存储文件夹",os.getcwd())  # 返回选择文件的名字
        print(filenames)
        self.file_dir_show.setPlainText(filenames)

    def tishi(self):
        QMessageBox.about(self, "    提示", "恭喜您，合并完成！！  \n\n请查阅" + dst_path_output + "文件")

    def error_not_found(self):
        QMessageBox.warning(self, "警告！","您指定的文件夹错误！！"  "\n\n  请重新选择")

    #重新设置路径
    def set_rename_data_dir(self,outputdir):
        outputdir = outputdir.replace('/', '')
        return outputdir


        #self.file_dir_show.setPlainText(outputdir)

    def rename_tishi(self,outputdir):
        outputdir = outputdir.replace('/', '')
        QMessageBox.about(self, "    提示", "恭喜您，重命名完成！！  \n\n请查阅" + outputdir + "文件夹")


dst_path_output = 'system_result.xlsx'  #最终输出的文件


#txt转excel的类
class txtToExcel():
    # def __init__(self):
    #     super(txtToExcel, self).__init__()
    #     self.setupUi(self)

    @classmethod
    def transformation(self,file_Name_Src_hanshu):  # 读取数据、转换格式，转成一维数组，然后在每个元素的中间都加上换行符
        try:
            data_Read = pd.read_table(file_Name_Src_hanshu, header=None, delimiter="\t")
            data_Read_Np = data_Read.to_numpy()
            data_Read_Array = list(np.array(data_Read_Np).flatten())
            flgeStart = 1
            while flgeStart < len(data_Read_Array):  # 还可优化
                data_Read_Array.insert(flgeStart, '\n')
                flgeStart += 2
            return data_Read_Array
        except Exception as ex:
            print(ex)

    @classmethod
    def flag_bit(self,data_Read_Array_hanshu):  # 获取标志位
        data_Read_Array = data_Read_Array_hanshu
        flagNumber = []
        try:
            for x in range(len(data_Read_Array)):
                target_str = re.match("检查项", data_Read_Array[x])
                if target_str != None:
                    flagNumber.append(x)
            flagNumber.append(len(data_Read_Array))
            return flagNumber
        except Exception as ex:
            print(ex)

    @classmethod
    def merge_hebing(self,flagNumber_hanshu,data_Read_Array_hanshu):
        flagNumber = flagNumber_hanshu
        data_Read_Array = data_Read_Array_hanshu
        end_Data_Read = []
        for x in range(len(flagNumber) - 1):
            end_Data_Read.append(''.join(data_Read_Array[slice(flagNumber[x], flagNumber[x + 1], 1)]))
        return end_Data_Read

    @classmethod
    def txt_to_excel_run(self,src_dir_input):
        #src_dir_input = 'E:/code/python_qt/rwapgui/src'
        src_Path = src_dir_input + '/'
        ip_Address = []
        file_Name_Src_List = []
        end_Data_Read_Huizong = []

        if src_dir_input == '':
            Show_Main().error_not_found()
        else:
            for root, dirs, files in os.walk(src_Path):
                try:
                    for i in files:
                        file_Name_Src = src_Path + i
                        file_Name_Src_List.append(file_Name_Src)
                        ip = file_Name_Src.replace(src_Path, '').replace('.txt', '')
                        ip_Address.append(ip)
                        # print("第一个函数：",transForMation(file_Name_Src))
                        # print("第二个函数：",flagBit(transForMation(file_Name_Src)) )
                        # print("第三个函数：",mergeHeBing(flagBit(transForMation(file_Name_Src)),transForMation(file_Name_Src)))
                        print(ip + "  Success!")
                        end_Data_Read_Huizong.append(txtToExcel().merge_hebing(txtToExcel().flag_bit(txtToExcel().transformation(file_Name_Src)),
                                                                               txtToExcel().transformation(file_Name_Src)))
                except:
                    pass

            zidian = dict(zip(ip_Address, end_Data_Read_Huizong))
            # print(zidian)
            df = pd.DataFrame(zidian)
            # print(df)
            # print(zidian)
            df.to_excel(dst_path_output, '安全通用要求-操作系统安全', index=False)
            if zidian == {}:
                print("警告:您指定的文件夹未发现合适的文件！！")
                cuo = "错误"
                Show_Main().error_not_found()
            else:
                print("\n" + "已完成全部内容的合并！！")
                Show_Main().tishi()



outputdir = 'refile_data/' #存放重命名后的文件夹

class renamefile():
    def renamef(self,src_dir_input):
        src_path = src_dir_input + '/'
        #outputdir = 'refile_data/'
        ip = []  # 用于存储ip地址
        file_name_src_list = []  # 用于存储文件路径
        if src_dir_input == '':
            Show_Main().error_not_found()
        else:
            try:
                for root, dirs, files in os.walk(src_path):
                    for file in dirs:
                        file1 = file + "/out.txt"
                        file_name_src_list.append(os.path.join(root, file1))
                        ip.append(file)

                file_name_src_list = file_name_src_list[(len(file_name_src_list) // 2):len(file_name_src_list)]
                ip = ip[0:(len(ip) // 2)]

                if os.path.exists(outputdir):  # 如果存在data_sql就先删除，以确保数据是最新的，而不是在原来的基础上添加的
                    shutil.rmtree(outputdir)
                if not os.path.isdir(outputdir):  # 如果没有文件夹data_sql，就会自己创建一个
                    os.makedirs(outputdir)

                for i in range(len(file_name_src_list)):
                    os.rename(file_name_src_list[i], outputdir + ip[i] + ".txt")
                    print(ip[i] + "  Success!!")

                Show_Main().set_rename_data_dir(outputdir)
                Show_Main().rename_tishi(outputdir)

            except:
                Show_Main().error_not_found()


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
