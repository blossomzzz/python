#!/usr/bin/python3


from tkinter import  *
import tkinter.messagebox
import os
import shutil
import time

root=Tk()
root.title("批量删除工具 - By ZhangHao")
root.geometry('480x320')

def confirm():
    confirm = tkinter.messagebox.askquestion('提示', '确定删除不在list里的文件')
    if confirm=='yes':
        files_rm()


def files_rm():
    cfg=cfg_path.get().split('list.txt')
    os.chdir(cfg[0])
    enblist=open(cfg[0]+'\list.txt','r',encoding='utf-8').read().splitlines()
    print(enblist)
    files=file_path.get()
    os.chdir(files)
    filename=os.listdir(files)
    start=round(time.time(),1)
    for enbid  in filename:
        if enbid not in enblist:
            global log
            log = ('正在删除: '+str(enbid))
            print(log)
            printinfo.set(log)
            shutil.rmtree(str(enbid))
    end=round(time.time(),1)

    log=('删除成功, 耗时: %s S!' %(end-start))
    print(log)
    printinfo.set(log)

def use_direction():
    direction = Toplevel(root)
    direction.geometry('440x180')
    direction.title('使用说明')
    Label(direction, text='功能: 删除不在配置文件(list.txt）内的目录和文件',justify=LEFT,fg='blue').place(x=60, y=40)
    Label(direction, text='说明: 1.配置文件为list.txt格式', justify=LEFT,fg='red').place(x=60, y=80)
    Label(direction, text='        2.要保存的目录名和文件名单行存入list.txt', justify=LEFT,fg='red').place(x=60, y=100)
    Label(direction, text='        3.确保路径正确，否则会误删文件（无法恢复）', justify=LEFT,fg='red').place(x=60, y=120)

'''def use_direction():
    direction = Toplevel(root)
    direction.geometry('440x180')
    direction.title('使用说明')
    canvas = tkinter.Canvas(direction, height=200, width=500).place(x=0, y=0)
    image_file = PhotoImage(file='E:\\Python\\zhanghao\\BatchDelete\\user.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
'''


cfg_path=StringVar()
cfg_path.set('E:\\list.txt')

file_path=StringVar()
file_path.set('D:\\CHENGDU\\20180311')

printinfo=StringVar()


button1 = Button(root,text='开始清理',fg='red',command=confirm).place(x=400,y=60)
button2 = Button(root,text='使用说明',fg='blue',command=use_direction).place(x=320,y=60)

#button2 = Button(root,text='工参路径',fg='black',activebackground='black',command=cfg_path).place(x=120,y=20)

#button3 = Button(root,text='文件路径',fg='black',activebackground='black',command=file_path).place(x=120,y=60)

Label(root,text='工参路径：').place(x=60,y=40)
Label(root,text='文件路径：').place(x=60,y=80)
Label(root, textvariable=printinfo, font=('Arial', 12), width=30,
             height=2).place(x=90,y=150)
entry_cfgpath=Entry(root,textvariable=cfg_path).place(x=120,y=40)
entry_filepath=Entry(root,textvariable=file_path).place(x=120,y=80)



root.mainloop()


