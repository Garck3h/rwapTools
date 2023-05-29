# rwapTools
这是一个多功能的GUI工具，可以实现批量整理绿盟RSAS扫描器的结果、实现整理基线的结果、实现达梦数据库的基线等

###漏扫基线
漏扫基线通过读取多个主机的excel，提取关键的字段信息合并到一个新的excel表格中
![image](https://github.com/Garck3h/rwapTools/assets/104743791/38a80d0b-065b-4d4c-8d4c-f5765572bedb)


###操作系统基线
操作系统基线，通过选择等保级别，从而会上传不同的sh脚本到远程服务器中，进行执行，然后把结果拉到本地，并且以IP命名。
然后通过整理，把txt文件根据关键字进行匹配，最终把所有主机的信息整合到一个新的excel表中。
![image](https://github.com/Garck3h/rwapTools/assets/104743791/f67f8741-edc5-4a37-a712-14819ee51db8)


###达梦数据库
达梦数据库是调用了disql命令来执行达梦的命令，读取sql文件为需要执行的sql语句。
从资产表中读取达梦数据库的信息，先进行测试连接，可以知道账号密码是否正确。
然后批量执行SQL语句，然后把txt结果输出到一个文件夹中。在window下执行需要转换一下为utf-8的格式。
最终根据关键字匹配分割，把全部结果整理到exce表格中。
![image](https://github.com/Garck3h/rwapTools/assets/104743791/8b97909b-aae3-4d55-bb7e-38debffc2155)


###其它
这个功能是比较自由的，自定义匹配的关键字作为分割点，然后分割为一个字段之后，继续循环，最终可以把一个txt文件转为excel文件。
![image](https://github.com/Garck3h/rwapTools/assets/104743791/a000247e-6a5f-4f23-9bf5-88ea4fb17de0)
