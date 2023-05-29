#Creation time：2022/10/17
#Author：garck
#用途：将基线结果整理到excel中
import os
import pandas as pd
import numpy as np
import re

def transForMation(file_Name_Src_hanshu):
    try:
        data_Read = pd.read_table(file_Name_Src_hanshu, header=None, delimiter="\t")
        data_Read_Np = data_Read.to_numpy()
        data_Read_Array = list(np.array(data_Read_Np).flatten())
        flgeStart = 1
        while flgeStart < len(data_Read_Array):   #还可优化
            data_Read_Array.insert(flgeStart, '\n')
            flgeStart += 2
        return data_Read_Array
    except Exception as ex:
        print(ex)

def flagBit(data_Read_Array_hanshu):
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

def mergeHeBing(flagNumber_hanshu,data_Read_Array_hanshu):
    flagNumber = flagNumber_hanshu
    data_Read_Array = data_Read_Array_hanshu
    end_Data_Read = []
    for x in range(len(flagNumber) - 1):
        end_Data_Read.append(''.join(data_Read_Array[slice(flagNumber[x], flagNumber[x + 1], 1)]))
    return end_Data_Read

if __name__ == '__main__':

    src_dir_input = 'E:/code/python_qt/rwapgui/src'
    src_Path = src_dir_input + '/'
    ip_Address = []
    file_Name_Src_List = []
    end_Data_Read_Huizong = []

    for root, dirs, files in os.walk(src_Path):
        for i in files:
            file_Name_Src = src_Path + i
            file_Name_Src_List.append(file_Name_Src)
            ip = file_Name_Src.replace(src_Path, '').replace('.txt', '')
            ip_Address.append(ip)
            # print("第一个函数：",transForMation(file_Name_Src))
            # print("第二个函数：",flagBit(transForMation(file_Name_Src)) )
            # print("第三个函数：",mergeHeBing(flagBit(transForMation(file_Name_Src)),transForMation(file_Name_Src)))
            print(ip + "  Success!")
            end_Data_Read_Huizong.append(
                mergeHeBing(flagBit(transForMation(file_Name_Src)), transForMation(file_Name_Src)))

    zidian = dict(zip(ip_Address, end_Data_Read_Huizong))
    # print(zidian)
    df = pd.DataFrame(zidian)
    # print(df)
    #print(zidian)
    df.to_excel("piliang.xlsx", '安全通用要求-操作系统安全', index=False)
    if zidian == {}:
        print("警告:您指定的文件夹未发现合适的文件！！")
    else:
        print("\n" + "已完成全部内容的合并！！")






