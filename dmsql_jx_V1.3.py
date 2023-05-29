#coding=utf-8

import xlrd
import os
import pandas as pd
import numpy as np
import re
import chardet
import codecs
import getopt
import sys
import subprocess



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
        print(passwd)
        print(port)

        comd = disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c exit"
        for i in range(len(ip_adress)):
            lianjie_ceshi().TestConnection(comd,ip_adress[i],port[i])







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
                print("失败")
        except Exception as e:
            # print(e)
            print(ip,":",port," -----")


    @classmethod
    def read_get_Data(self,input_dir_name,input_disql,input_sql,input_file):
        print("\n")
        print("获取情况：")
        dir_name = input_dir_name
        disql = input_disql
        sql = input_sql
        input_file = input_file

        if not os.path.isdir(dir_name):  # 如果没有文件夹src，就会自己创建一个
            os.makedirs(dir_name)

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
        print(passwd)
        print(port)

        for i in range(len(ip_adress)):
            get_Data.TestConnection(disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " "+ "-c exit",disql + " " + username[i] + "/" + passwd[i] + "@" + ip_adress[i] + ":" + str(port[i]) + " " + "`" +sql
                         + ">>" + "./" + dir_name + "/" + ip_adress[i] + "-" + str(port[i]) + ".txt",ip_adress[i],port[i])


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




def run():
    dir_name = 'data'
    disql = 'D:/qax/dmdbms/bin/DIsql.exe'
    sql = 'D:/qax/dmjx/2.sql'
    file_input = 'E:/code/python_qt/rwapgui/passwd1.xlsx'


    #调用执行命令的函数，去查询数据库的内容。先尝试连接数据库，若连接成功则退出后，再连接再拉去数据；若连接失败则提升账号或者密码错误
    #连接类

    lianjie_ceshi().read_get_Data(disql,file_input)
    #获取数据类
    get_Data.read_get_Data(dir_name,disql,sql,file_input)
    #
    #
    # # 这里封装了一个将gbk文件转化成utf-8格式的文件的类，只需要调用类gbkToUtf8中的ReadDirectoryFile方法即可
    gbkToUtf8.ReadDirectoryFile(dir_name)


    #
    #
    src_path = dir_name + '/'
    ip_address_and_port = []  # 用于存储ip地址
    end_data_huizong = []  # 用于将所有的内容存在到里面，形成了一个二维数组，每个元素对应一个数组，即IP的内容，
    geshu = 0
    print("\n")
    print("result:")
    for root, dirs, files in os.walk(src_path):
        for i in files:
            file_name_src = src_path + i
            ip = file_name_src.replace(src_path, '').replace('.txt', '').replace('-', ':')
            print(ip,"  Success!")
            geshu = geshu + 1
            ip_address_and_port.append(ip)

            # print("第一个函数：",txtToExcel.transformation(file_name_src))
            # print("第二个函数：",txtToExcel.flag_bit(txtToExcel.transformation(file_name_src)) )
            # print("第三个函数：",merge_hebing(flag_bit(transformation(file_name_src)),transformation(file_name_src)))

            end_data_huizong.append(
                txtToExcel.merge_hebing(txtToExcel.flag_bit(txtToExcel.transformation(file_name_src)),
                                        txtToExcel.transformation(file_name_src)))
    # 将IP和全部数据的二维数组构造成一个字典
    zidian = dict(zip(ip_address_and_port, end_data_huizong))
    #print(zidian)
    df = pd.DataFrame(zidian)
    # print(df)
    df.to_excel("result.xlsx", '安全通用要求-操作系统安全', index=False)
    print("\n" + "共完成了",geshu,"个数据库的合并")


if __name__ == '__main__':
    run()