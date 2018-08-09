# -*- coding: utf-8 -*-
import os
import shutil
import time
import sys

type=input('输入保留MR格式|MRO|MRE|MRS:')
cfg_name=input('输入列表文件名：')
cfg_path=input('输入列表文件路径：')
file_path=input('输入删除文件路径：')

os.chdir(file_path)
enblist=list(map(str,open(cfg_path+cfg_name,encoding='utf-8').read().splitlines()))
print('保留文件名为：')
print(enblist)

filename=os.listdir(file_path)
start=round(time.time(),1)
for i in filename:
    m=i[8:11]
    if m !=type:
        print('正在删除非{}文件: {}'.format(type,i))
        os.remove(file_path + i)

    else:

        x=i[19:25]
        if x  not in enblist:
            print(x)
            if os.path.isfile(file_path+i):
                log = ('正在删除: ' + i)
                print(log)
                os.remove(file_path+i)
            else:
                log = ('正在删除: ' + i)
                print(log)
                shutil.rmtree(str(i))
end = round(time.time(), 1)
long = ('删除成功, 耗时: %s S!' % (end - start))
print(long+'\n')
T=input('Done ! 按回车键退出。')
if T:
    sys.exit()



