# coding=gbk
# Purpose : 1.Connect to  remote host to execute commands
#           2.Download files with FTP
#           3.Load data to Oracle
# Coder  :  ZhangHao

import csv
import cx_Oracle
import os
from ftplib import FTP


cfg_ftp={'host':'192.168.17.224',
         'port':22,
         'username':'root',
         'password':'Richr00t'}

info1={'username':'c##zhanghao',
            'password':'zhanghao',
            'host':'ORCL'}

def ftp():
    ftp=FTP()
    ftp.connect(cfg_ftp['host'],cfg_ftp['port'])
    ftp.login(cfg_ftp['username'],cfg_ftp['password'])
    print('已连接到主机：'+cfg_ftp['host'])

ftp()

def oracle():
    db = cx_Oracle.connect(info1['username'],info1['password'],info1['host'])
    print('连接到数据库: ' + info1['host'])
    cursor = db.cursor()

    with open('E:\\test.csv','r',encoding='utf-8') as csvfile:
            read=csv.reader(csvfile)
            info = [i for i in read]
            title = info[0]
            data = info[1:]

            for x in data:
                try:
                    x0= '\'' + x[0] + '\''
                except Exception as e:
                    x0= 'null'

                try:
                    x1 = '\''+x[1].split()[0]+'\''
                except Exception as e:
                    x1 = 'null'

                try:
                    x2 = '\''+x[2].split()[0]+'\''
                except Exception as e:
                    x2 = 'null'

                try:
                    x3 ='\''+x[3].split()[0]+'\''
                except Exception as e:
                    x3 = 'null'

                try:
                    x4 = '\''+x[4].split()[0]+'\''
                except Exception as e:
                    x4 = 'null'

                try:
                    x5 ='\''+x[5].split()[0]+'\''
                except Exception as e:
                    x5 = 'null'

                try:
                    x6 = '\''+x[6].split()[0]+'\''
                except Exception as e:
                    x6 = 'null'

                try:
                    x7 = '\'' + x[7].split()[0] + '\''
                except Exception as e:
                    x7 = 'null'

                try:
                    x8 = '\'' + x[8].split()[0] + '\''
                except Exception as e:
                    x8 = 'null'

                try:
                    x9 = '\'' + x[9].split()[0] + '\''
                except Exception as e:
                    x9 = 'null'

                try:
                    x10 = '\'' + x[10].split()[0] + '\''
                except Exception as e:
                    x10 = 'null'

                try:
                    x11 = '\'' + x[11].split()[0] + '\''
                except Exception as e:
                    x11 = 'null'

                try:
                    x12 = '\'' + x[12].split()[0] + '\''
                except Exception as e:
                    x12 = 'null'

                try:
                    x13 = '\'' + x[13].split()[0] + '\''
                except Exception as e:
                    x13 = 'null'

                try:
                    x14 = '\'' + x[14].split()[0] + '\''
                except Exception as e:
                    x14 = 'null'

                try:
                    x15 = '\'' + x[15].split()[0] + '\''
                except Exception as e:
                    x15 = 'null'

                try:
                    x16 = '\'' + x[16].split()[0] + '\''
                except Exception as e:
                    x16 = 'null'

                try:
                    x17 = '\'' + x[17].split()[0] + '\''
                except Exception as e:
                    x17 = 'null'

                try:
                    x18 = '\'' + x[18].split()[0] + '\''
                except Exception as e:
                    x18 = 'null'

                try:
                    x19 = '\'' + x[19].split()[0] + '\''
                except Exception as e:
                    x19 = 'null'

                try:
                    x20 = '\'' + x[20].split()[0] + '\''
                except Exception as e:
                    x20 = 'null'

                try:
                    x21 = '\'' + x[21].split()[0] + '\''
                except Exception as e:
                    x21 = 'null'

                try:
                    x22 = '\'' + x[22].split()[0] + '\''
                except Exception as e:
                    x22 = 'null'

                try:
                    x23 = '\'' + x[23].split()[0] + '\''
                except Exception as e:
                    x23 = 'null'

                try:
                    x24 = '\'' + x[24].split()[0] + '\''
                except Exception as e:
                    x24 = 'null'

                try:
                    x25 = '\'' + x[25].split()[0] + '\''
                except Exception as e:
                    x25 = 'null'

                try:
                    x26 = '\'' + x[26].split()[0] + '\''
                except Exception as e:
                    x26 = 'null'

                try:
                    x27 = '\'' + x[27].split()[0] + '\''
                except Exception as e:
                    x27 = 'null'

                try:
                    x28 = '\'' + x[28].split()[0] + '\''
                except Exception as e:
                    x28 = 'null'

                try:
                    x29 = '\'' + x[29].split()[0] + '\''
                except Exception as e:
                    x29 = 'null'

                try:
                    x30 = '\'' + x[30].split()[0] + '\''
                except Exception as e:
                    x30 = 'null'

                try:
                    x31 = '\'' + x[31].split()[0] + '\''
                except Exception as e:
                    x31 = 'null'

                try:
                    x32 = '\'' + x[32].split()[0] + '\''
                except Exception as e:
                    x32 = 'null'

                try:
                    x33 = '\'' + x[33].split()[0] + '\''
                except Exception as e:
                    x33 = 'null'

                try:
                    x34 = '\'' + x[34].split()[0] + '\''
                except Exception as e:
                    x34 = 'null'

                try:
                    x35 = '\'' + x[35].split()[0] + '\''
                except Exception as e:
                    x35 = 'null'

                try:
                    x36 = '\'' + x[36].split()[0] + '\''
                except Exception as e:
                    x36 = 'null'

                try:
                    x37 = '\'' + x[37].split()[0] + '\''
                except Exception as e:
                    x37 = 'null'

                try:
                    x38 = '\'' + x[38].split()[0] + '\''
                except Exception as e:
                    x38 = 'null'






                print(x0,x1,x2,x3,x4,x5,x6)


                sql = 'insert into radio_kqi  values ({},{},{},{},{},{},{},{},{},{},{},{},{},{},' \
    '{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})'.format(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,
                                                                       x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,
                                                                       x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,
                                                                       x31,x32,x33,x34,x35,x36,x37,x38)
                print(sql)
                cursor.execute(sql)
                db.commit()



