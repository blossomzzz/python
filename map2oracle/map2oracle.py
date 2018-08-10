#!/usr/bin/python3
#coding:utf-8
#coder:HaoZhang

import os

path='C:\\Users\\HAO\\Desktop\\zidonghua\\'   #txt地图文件路径
user='fast'                                   #oracle账户
pwd='fast*123'                                #oracle密码
sid='fast'                                    #oracle实例

def loader(path):
    filelist=os.listdir(path)
    for file in filelist:
        (filename,extension)=os.path.splitext(file)
        if extension=='.ctl':
            ctl_name=filename
            os.system('SQLLDR {}/{}@{} control = {}'.format(user,pwd,sid,ctl_name))
            print('正在入库 ...')


if __name__ == '__main__':
    os.chdir(path)
    loader(path)
    print('入库完成 !')