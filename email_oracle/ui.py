#!/usr/bin/python3
# -*- coding: utf-8 -*-
# by zhanghao

from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QFileDialog,QTextEdit, QHBoxLayout, QVBoxLayout
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import cx_Oracle
import datetime
import time

class Mywindow(QMainWindow):       #创建窗口类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500,300,500,300)
        self.setWindowTitle('email监控oracle工具')

        self.statusBar().showMessage('准备就绪...')

        self.bt1=QPushButton('选择SQL',self)
        self.bt1.move(350,50)

        self.bt2=QPushButton('输出路径',self)
        self.bt2.move(350,100)

        self.bt3=QPushButton('开始',self)
        self.bt3.move(100,200)

        self.bt4=QPushButton('暂停',self)
        self.bt4.move(300,200)

        self.bt1.clicked.connect(self.connect_oracle)
        self.bt2.clicked.connect(self.choosepath)
        self.bt3.clicked.connect(self.send_email)
        self.bt4.clicked.connect(self.pause)

        self.show()

    def connect_oracle(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './', ("Text  files (*.txt)"))
        if fname[0]:
            self.setStatusTip('已选择查询SQL')
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

    def send_email(self):
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


    def choosepath(self):
        pname = QFileDialog.getSaveFileName(self, '选择文件', './', "Text files (*.txt)")
        if pname[0]:
            self.setStatusTip('已选择路径')
            with open(pname[0], 'w', encoding='utf-8', errors='ignore') as f:
                f.write(self.tx.toPlainText())

    def pause(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mywindow()
    sys.exit(app.exec_())