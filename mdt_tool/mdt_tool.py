#coding=utf-8
#coder:HaoZhang
#1.合并多个大MDT文件(csv)
#2.为tdlte_mdt添加表头和填充type值(默认type=3)
#3.计算mdt采样点离基站的距离，清洗异常采样点(>3KM)

import numpy as np
import pandas as pd
import os
import time

type=3
dis_enb=3

now_path=os.getcwd()
csv_path=now_path + r'\csv'                          #原始MDT文件存放路径
out_path1=now_path + r'\output\tdlte_dt1.csv'        #合并后MDT文件存放路径
out_path2=now_path + r'\output\tdlte_dt2.csv'        #清洗后MDT文件存放路径（含dis）
out_path=now_path + r'\output\tdlte_dt.csv'          #最终MDT文件存放路径
cfg_path=now_path + r'\config\cfg_enb.csv'           #工参存放路径

columns=['Time','Longitude','Latitude','RSRP','eNB_ID','SCell CellID','Sector','EARFCN','Scell PCI',
         'NCell RSRP_1','NCell RSRP_2','NCell RSRP_3','NCell RSRP_4','NCell RSRP_5','NCell RSRP_6',
         'NCell RSRP_7','NCell RSRP_8','NCell RSRP_9','NCell EARFCN_1','NCell EARFCN_2','NCell EARFCN_3',
         'NCell EARFCN_4','NCell EARFCN_5','NCell EARFCN_6','NCell EARFCN_7','NCell EARFCN_8','NCell EARFCN_9',
         'NCell PCI_1','NCell PCI_2','NCell PCI_3','NCell PCI_4','NCell PCI_5','NCell PCI_6',	'NCell PCI_7',
         'NCell PCI_8','NCell PCI_9','DL_RATE','DL_SINR','DL_CQI','TYPE']


def haversine(lon1, lat1, lon2, lat2):
    MILES = 3959
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance = MILES * c * 1.609344     #KM
    return distance


def combine_csv():
    os.chdir(csv_path)
    csv_list=os.listdir()
    df=pd.read_csv(csv_path + '\\' + csv_list[0],encoding='utf-8',names=columns)
    df.to_csv(out_path1,encoding='utf-8', index=False)
    for i in range(1,len(csv_list)):
        df=pd.read_csv(csv_path + '\\' + csv_list[i],encoding='utf-8')
        df.to_csv(out_path1, encoding="utf-8", index=False, header=False, mode='a+')


def add_type():
    df=pd.read_csv(out_path1,encoding='utf-8')
    df.loc[:, "TYPE"] = type
    df.to_csv(out_path1,encoding="utf-8",index=False)



def clean_data():
    df1=pd.read_csv(out_path1,encoding='utf-8')
    df2=pd.read_csv(cfg_path,encoding='utf-8')

    rs=pd.merge(df1,df2,on='SCell CellID',how='left')

    dis=(haversine(rs['Longitude'],rs['Latitude'],rs['Lon'],rs['Lat']))

    df1['DIS']=dis
    df1=df1[df1['DIS'] < dis_enb]
    df1.to_csv(out_path2,index=False)

    df1.drop(['DIS'],axis=1,inplace=True)
    df1.to_csv(out_path, index=False)

time1 = time.time()
print('数据处理中...')
combine_csv()
time2 = time.time()
cost1=time2-time1
print('合并CSV文件完成,耗时：{} S !!!'.format(round(cost1, 2)))
add_type()
time3 = time.time()
cost2=time3-time2
print('表头和字段处理完成,耗时：{} S !!!'.format(round(cost2, 2)))
clean_data()
time4 = time.time()
cost3=time4-time3
print('数据清洗完成,耗时：{} S !!!'.format(round(cost3, 2)))
print('*'*20)
print('数据已保存到output文件夹下！')


