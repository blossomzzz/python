# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import cx_Oracle
import datetime
import time
from PyQt5.QtWidgets import QMainWindow,QFileDialog

class function(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def connect_oracle():
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', ("Text  files (*.txt)"))
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as file:
                sqlall = file.read().split(';')
                db = cx_Oracle.connect('sqmdb', 'mdasil', '192.168.17.224:1521/sqmmt')
                print('oracle version :' + db.version)
                cursor = db.cursor()

                for sql in sqlall:
                    #print(sql)
                    cursor.execute(sql)
                    row = str(cursor.fetchone())
                    with open('E:\\info.txt', 'a+',encoding='utf-8') as f:
                        f.write(row+'\n')


    def send_email():
        smtpserver = 'smtp.163.com'
        sender = 'hao_3_zhang@163.com'
        receiver = 'hao.3.zhang@nokia-sbell.com'

        username = 'hao_3_zhang@163.com'
        password = 'zh1017345300'
        subject = '自动监控'

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = 'world<hello>'
        msg['To'] = "hao.3.zhang@nokia-sbell.com"
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8')) #正文

        att1 = MIMEText(open('E:\\info.txt', 'rb').read(), 'base64', 'utf-8') #附件
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="info.txt"'
        msg.attach(att1)

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print('Done !')
        smtp.quit()
