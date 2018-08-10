#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:14:12 2018

@author: HaoZhang
"""
import os
import os.path
import re
import pandas as pd



pattern=re.compile(r'.*_(.*)_(.*)_(.*)_(.*)_([0-9]{8}).*')

# countnum=dict()
# countsize=dict()

category_list=[]
vender_list=[]
enb_list=[]
sdate_list=[]
size_list=[]

#
# def counter_num(kind):
#     if kind in countnum:
#         countnum[kind] += 1
#     else:
#         countnum[kind] = 1
#
# def counter_size(kind,size):
#     if kind in countsize:
#         countsize[kind] += size
#     else:
#         countsize[kind] = size

def get_details(path):
    fileList = os.listdir(path)  
    for filename in fileList:
        pathTmp = os.path.join(path,filename)  

        if os.path.isdir(pathTmp):
            get_details(pathTmp)

        elif os.path.isfile(pathTmp) and str(pattern.match(filename)) !='None' : 
            filesize = os.path.getsize(pathTmp)  

            match=pattern.match(filename)

            category=match.group(1)
            vender=match.group(2)
            enb=match.group(4)
            sdate=match.group(5)

            category_list.append(category)
            vender_list.append(vender)
            enb_list.append(enb)
            sdate_list.append(sdate)
            size_list.append(round(filesize/1024,2))

            # counter_num(category)
            # counter_num(vender)
            # counter_num(sdate)
            #
            # counter_size(category,filesize)
            # counter_size(vender,filesize)
            # counter_size(sdate,filesize)

def to_excel():

    d={'格式':pd.Series(category_list),
        '厂家': pd.Series(vender_list),
        'enb': pd.Series(enb_list),
        '大小（KB）': pd.Series(size_list),
        '日期': pd.Series(sdate_list)}

    df1=pd.DataFrame(d)
    df1['enb']=df1['enb'].astype(int)
    df2 =pd.read_table(enbpath, names=['enb'])




    df3 =df1.groupby(by=['enb'])['大小（KB）'].sum()
    df4 =df1.groupby(by=['格式'])['大小（KB）'].sum()
    df5 =df1.groupby(by=['日期'])['大小（KB）'].sum()

    rs = pd.merge(df2, df1, on='enb', how='left')
    rs = rs[rs.T.isnull().any()]
    rs.drop(['格式','厂家','大小（KB）','日期'], axis=1, inplace=True)

    df1.to_excel(writer, 'MR详单',index=False)
    df2.to_excel(writer, '基站工参',index=False)
    df3.to_excel(writer, '按基站分组')
    df4.to_excel(writer, '按格式分组')
    df5.to_excel(writer, '按日期分组')

    rs.to_excel(writer, '缺失MR的基站',index=False)

    writer.save()



outpath=r'/home/check_result.xlsx'
writer = pd.ExcelWriter(outpath)

enbpath=input("输入基站列表路径(如 /home/dispatcherthreadmain/LUZHOU)：").strip()

path=input("输入MR存放路径(如 /home 或者 /home/MR_RAW_DAY20180801)：").strip()

try:
    print('='*50)
    print('数据核查开始...')
    get_details(path)
    print('正在生成核查表...')
    to_excel()
    writer.close()
    print('='*50)
    print('核查结束，结果表已保存到：/home/check_result.xlsx')
except Exception as e:
    print('=' * 50)
    print('请检查路径输入是否有误！！！')


