from PyQt5.QtWidgets import QFileDialog,QMessageBox
import os
import pandas as pd
import numpy as np
import re
import System_Ui
import shutil
import time
from openpyxl import load_workbook
import paramiko
import scp
import argparse


class System_Function(System_Ui.System_uimian):

    def __init__(self):
        super(System_Function, self).__init__()

    def system_Implement(self):
        #批量整理结果
        # 选择文件夹
        self.system_file_btn.clicked.connect(lambda: self.system_loadDir())
        # 批量重命名
        self.system_rename_btn.clicked.connect(lambda: renamefile().renamef(self.system_lineEdit.text()))
        self.system_rename_btn.clicked.connect(lambda: self.system_lineEdit.setText(outputdir.replace('/', '')))

        # txt转excel的按钮
        self.system_start_btn.clicked.connect(lambda: txtToExcel().txt_to_excel_run(self.system_lineEdit.text()))

        ###批量执行基线
        #选中资产按钮
        self.Baseline_file_btn.clicked.connect(lambda: self.load_property())
        #开始批量检查的按钮
        self.Baseline_Start_Btn.clicked.connect(lambda: baseline().baselinemain(self.Baseline_lineEdit.text(),self.Baseline_level.currentText()))
        self.Baseline_Start_Btn.clicked.connect(lambda: self.system_lineEdit.setText("baseline_result"))




    def system_loadDir(self):
        filenames = QFileDialog.getExistingDirectory(None, "选择存储文件夹", os.getcwd())  # 返回选择文件的名字
        if filenames:
            self.system_lineEdit.setText(filenames)

    def tishi(self):
        QMessageBox.about(self, "    提示", "恭喜您，合并完成！！  \n\n请查阅" + dst_path_output + "文件")

    def error_not_found(self):
        QMessageBox.warning(self, "警告！", "您指定的文件夹错误！！"  "\n\n  请重新选择")

    # 重新设置路径
    def set_rename_data_dir(self, outputdir):
        outputdir = outputdir.replace('/', '')
        return outputdir

        # self.file_dir_show.setPlainText(outputdir)

    def rename_tishi(self, outputdir):
        outputdir = outputdir.replace('/', '')
        QMessageBox.about(self, "    提示", "恭喜您，重命名完成！！  \n\n请查阅" + outputdir + "文件夹")

    def load_property(self):  # 选择资产文件的函数   getOpenFileName(self, "打开文件", '.', '图像文件(*.jpg *.png)')
        filenames, _ = QFileDialog.getOpenFileName(self, "打开文件", '.', 'xlsx文件(*.xlsx *.xls)')  # 返回选择文件的名字
        if filenames:
            self.Baseline_lineEdit.setText(filenames)
            print("\n选择资产文件：", filenames)

    def Baseline_check_completed(self,Baseline_result):
        QMessageBox.about(self, "    提示", "恭喜您，完成了批量基线检查！！  \n\n请查阅" + Baseline_result + "文件夹")

    def Baseline_property_not_found(self):
        QMessageBox.warning(self, "警告！", "请选择资产文件")


dst_path_output = 'system_result.xlsx'  #最终输出的文件


#txt转excel的类
class txtToExcel():
    # def __init__(self):
    #     super(txtToExcel, self).__init__()
    #     self.setupUi(self)

    @classmethod
    def transformation(self,fileNameSrcHanshu):  # 读取数据、转换格式，转成一维数组，然后在每个元素的中间都加上换行符
        try:
            data2 = []
            readf = open(fileNameSrcHanshu, 'r', encoding='utf-8')
            for data in readf.readlines():
                # data1 = re.sub('\t|\n', '', data)
                data1 = re.sub('\t', '   ', data)
                data1 = re.sub('\n', '', data1)
                data1 = data1.split('\n')
                data2.append(data1)
            data_Read_Array = np.array(data2).flatten()
            #flgeStart = 1
            # while flgeStart < len(data_Read_Array):  # 还可优化
            #     data_Read_Array.insert(flgeStart, '\n')
            #     flgeStart += 2
            #     print(data_Read_Array)

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
            end_Data_Read.append('\n'.join(data_Read_Array[slice(flagNumber[x], flagNumber[x + 1], 1)]))
        return end_Data_Read

    @classmethod
    def txt_to_excel_run(self,src_dir_input):
        #src_dir_input = 'E:/code/python_qt/rwapgui/src'
        src_Path = src_dir_input + '/'
        ip_Address = []
        file_Name_Src_List = []
        end_Data_Read_Huizong = []

        if src_dir_input == '':
            print("2")
            System_Function().error_not_found()
        else:
            for root, dirs, files in os.walk(src_Path):
                try:
                    for i in files:
                        file_Name_Src = src_Path + i
                        file_Name_Src_List.append(file_Name_Src)
                        ip = file_Name_Src.replace(src_Path, '').replace('.txt', '')
                        ip_Address.append("(操作系统：Linux;IP:" + ip + ")测评记录")
                        #ip_Address.append(ip)
                        #print("第一个函数：",transForMation(file_Name_Src))
                        # print("第二个函数：",flagBit(transForMation(file_Name_Src)) )
                        # print("第三个函数：",mergeHeBing(flagBit(transForMation(file_Name_Src)),transForMation(file_Name_Src)))
                        #print(ip + "  Success!")

                        end_Data_Read_Huizong.append(txtToExcel().merge_hebing(txtToExcel().flag_bit(txtToExcel().transformation(file_Name_Src)),
                                                                               txtToExcel().transformation(file_Name_Src)))
                except:
                    pass

            zidian = dict(zip(ip_Address, end_Data_Read_Huizong))
            #df = pd.DataFrame(zidian) #原本的
            df = pd.DataFrame(pd.DataFrame.from_dict(zidian, orient='index').values.T, columns=list(zidian.keys()))  #防止输入的数值长度不一样的时候会崩掉
            df.to_excel(dst_path_output, '安全通用要求-操作系统安全', engine='xlsxwriter', index=False)
            if zidian == {}:
                #print("警告:您指定的文件夹未发现合适的文件！！")
                cuo = "错误"
                print("3")
                System_Function().error_not_found()
            else:
                #print("\n" + "已完成全部内容的合并！！")
                System_Function().tishi()


outputdir = 'refile_data/' #存放重命名后的文件夹



class renamefile():
    def renamef(self,src_dir_input):
        src_path = src_dir_input + '/'
        #outputdir = 'refile_data/'
        ip = []  # 用于存储ip地址
        file_name_src_list = []  # 用于存储文件路径
        if src_dir_input == '':
            System_Function().error_not_found()
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
                    #print(ip[i] + "  Success!!")

                System_Function().set_rename_data_dir(outputdir)
                System_Function().rename_tishi(outputdir)

            except:
                print("1")
                System_Function().error_not_found()



#批量进行基线检查
class baseline():
    def upload_file(self, hostname, username, password, port, local_path, remote_path,dir_name):
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname, username=username, password=password, port=port)

            # SCP上传文件到远程服务器
            with scp.SCPClient(ssh.get_transport()) as scp_client:
                scp_client.put(local_path, remote_path)

            # 添加权限并执行，将输出保存到文件
            # command = f"chmod +x {remote_path} && {remote_path} > /tmp/out1.txt 2>&1"
            print(remote_path)
            print(f"给脚本添加权限----------{hostname}")
            command = f"chmod +x {remote_path}"
            stdin, stdout, stderr = ssh.exec_command(command)

            # 检查是否有错误信息
            err = stderr.read().decode()
            if err != '':
                raise Exception(f"执行： {hostname} failed:\n{err}")

            # invoke = ssh.invoke_shell()
            # invoke.send("/tmp/linux_baseline_level3.sh")
            # time.sleep(30)  # 等待命令执行完毕
            print(f"权限添加完毕----------{hostname}")
            print(f"运行基线脚本----------{hostname}")
            stdin2, stdout2, stderr2 = ssh.exec_command(f"cd /tmp && /tmp/{local_path} &")  # 执行命令并获取命令结果
            # stdin为输入的命令
            # stdout为命令返回的结果
            # stderr为命令错误时返回的结果
            res, err = stdout2.read(), stderr2.read()
            result = res if res else err
            print(result.decode().strip())

            # 下载输出文件
            with scp.SCPClient(ssh.get_transport()) as scp_client:
                scp_client.get('/tmp/out.txt', "./"+dir_name + f"/{hostname}.txt")

            # 清楚遗留文件
            print(f"清除遗留文件----------{hostname}")
            stdin2, stdout2, stderr2 = ssh.exec_command(f"rm -rf  /tmp/{local_path} /tmp/out.txt")  # 执行命令并获取命令结果
            # stdin为输入的命令
            # stdout为命令返回的结果
            # stderr为命令错误时返回的结果
            res, err = stdout2.read(), stderr2.read()
            result = res if res else err
            print(f"清除完毕----------{hostname}")

    def baselinemain(self,filenamein,filenameshin):

        dir_name = "baseline_result"
        if os.path.exists(dir_name): #如果存在data_sql就先删除，以确保数据是最新的，而不是在原来的基础上添加的
            shutil.rmtree(dir_name)
        if not os.path.isdir(dir_name):  # 如果没有文件夹data_sql，就会自己创建一个
            os.makedirs(dir_name)

        if(filenameshin == "等保二级"):
            filenamesh = "linux_baseline_level2.sh"
        else:
            filenamesh = "linux_baseline_level3.sh"

        if(filenamein == ""):
            System_Function().Baseline_property_not_found()
        else:
            print("已选择资产："+ filenamein)

            # 读取Excel文件
            wb = load_workbook(filename=filenamein)
            ws = wb.active

            # 将Excel数据转换为DataFrame
            df = pd.DataFrame(ws.values)
            df.columns = ['host', 'port', 'username', 'password']

            local_file_path = filenamesh
            remote_file_path = '/tmp/' + filenamesh

            try:
                # 遍历每一行，上传文件并执行远程脚本，下载输出文件
                for index, row in df.iloc[1:].iterrows():
                    hostname = row['host']
                    port = str(row['port'])
                    username = row['username']
                    password = str(row['password'])

                    # print(hostname, username, password, port)
                    # print(type(hostname), type(username), type(password), type(port))

                    try:
                        baseline().upload_file(hostname, username, password, port, local_file_path, remote_file_path,
                                               dir_name)
                        print(f"执行完毕： {hostname} succeeded!")
                    except Exception as e:
                        print(e)
                    print("\n")
            except Exception as e:
                print(e)
            System_Function().Baseline_check_completed(dir_name)





