from PyQt5.QtWidgets import QFileDialog, QMessageBox
import Other_Ui
import os
import pandas as pd
import numpy as np
import re


class Other_Function(Other_Ui.Other_uimian):

    def __init__(self):
        super(Other_Function, self).__init__()

    def Other_Implement(self):
        self.other_filedir_btn.clicked.connect(lambda: self.Other_loadDir())
        # txt转excel的按钮
        self.other_start_btn.clicked.connect(lambda: txtToExcel().txt_to_excel_run(self.other_lineEdit_dir.text(),self.other_lineEdit_rule.text()))


    def Other_loadDir(self):
        filenames = QFileDialog.getExistingDirectory(None, "选择存储文件夹", os.getcwd())  # 返回选择文件的名字
        if filenames:
            self.other_lineEdit_dir.setText(filenames)

    def tishi(self):
        QMessageBox.about(self, "    提示", "恭喜您，合并完成！！  \n\n请查阅" + dst_path_output + "文件")

    def error_not_found1(self):
        QMessageBox.warning(self, "警告！", "请输入匹配的规则！！"  "\n\n  请重新选择")

    def error_not_found(self):
        QMessageBox.warning(self, "警告！", "您指定的文件夹错误！！"  "\n\n  请重新选择")



    # 重新设置路径
    def set_rename_data_dir(self, outputdir):
        outputdir = outputdir.replace('/', '')
        return outputdir

    def rename_tishi(self, outputdir):
        outputdir = outputdir.replace('/', '')
        QMessageBox.about(self, "    提示", "恭喜您，重命名完成！！  \n\n请查阅" + outputdir + "文件夹")




dst_path_output = 'other_result.xlsx'  #最终输出的文件

#txt转excel的类
class txtToExcel():
    # def __init__(self):
    #     super(txtToExcel, self).__init__()
    #     self.setupUi(self)

    @classmethod
    def transformation(self,fileNameSrcHanshu):  # 读取数据、转换格式，转成一维数组，然后在每个元素的中间都加上换行符
        try:
            # data_Read = pd.read_table(file_Name_Src_hanshu, header=None, delimiter="\t")
            # # data_Read = pd.read_table(file_Name_Src_hanshu, header=None, delimiter="\t", on_bad_lines='skip') #跳过错误行，一般是遇到了tab键
            # data_Read_Np = data_Read.to_numpy()
            # data_Read_Array = list(np.array(data_Read_Np).flatten())
            #flgeStart = 1
            # while flgeStart < len(data_Read_Array):  # 还可优化
            #     data_Read_Array.insert(flgeStart, '\n')
            #     flgeStart += 2
            data2 = []
            readf = open(fileNameSrcHanshu, 'r', encoding='utf-8')
            for data in readf.readlines():
                # data1 = re.sub('\t|\n', '', data)
                data1 = re.sub('\t', '   ', data)
                data1 = re.sub('\n', '', data1)
                data1 = data1.split('\n')
                data2.append(data1)
            data_Read_Array = np.array(data2).flatten()
            return data_Read_Array
        except Exception as ex:
            print(ex)

    @classmethod
    def flag_bit(self,data_Read_Array_hanshu,input_rule):  # 获取标志位
        data_Read_Array = data_Read_Array_hanshu
        flagNumber = []
        try:
            for x in range(len(data_Read_Array)):
                target_str = re.match(input_rule, data_Read_Array[x])
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
            #end_Data_Read.append(''.join(data_Read_Array[slice(flagNumber[x], flagNumber[x + 1], 1)]))
        return end_Data_Read

    @classmethod
    def txt_to_excel_run(self,src_dir_input,input_rule):
        src_Path = src_dir_input + '/'
        ip_Address = []
        file_Name_Src_List = []
        end_Data_Read_Huizong = []

        if src_dir_input == '':
            Other_Function().error_not_found()
        else:
            if input_rule == '':
                Other_Function().error_not_found1()
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
                            end_Data_Read_Huizong.append(txtToExcel().merge_hebing(txtToExcel().flag_bit(txtToExcel().transformation(file_Name_Src),input_rule),
                                                                                   txtToExcel().transformation(file_Name_Src)))
                    except:
                        pass

                zidian = dict(zip(ip_Address, end_Data_Read_Huizong))
                # print(zidian)
                #df = pd.DataFrame(zidian)
                df = pd.DataFrame(pd.DataFrame.from_dict(zidian, orient='index').values.T,
                                  columns=list(zidian.keys()))  # 防止输入的数值长度不一样的时候会崩掉
                # print(df)
                # print(zidian)
                df.to_excel(dst_path_output, '安全通用要求-操作系统安全', engine='xlsxwriter', index=False)
                if zidian == {}:
                    print("警告:您指定的文件夹未发现合适的文件！！")
                    cuo = "错误"
                    Other_Function().error_not_found()
                else:
                    print("\n" + "已完成全部内容的合并！！")
                    Other_Function().tishi()

