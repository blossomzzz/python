# myftp.py

from ftplib import FTP

class MyFTP(FTP):

    def getSubdir(self, *args):
        '''拷贝了 nlst() 和 dir() 代码修改，返回详细信息而不打印'''
        cmd = 'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            cmd = cmd + (' ' + arg)
        files = []
        self.retrlines(cmd, files.append)
        return files

    def getdirs(self, dirname=None):
        """返回目录列表，包括文件简要信息"""
        if dirname != None:
            self.cwd(dirname)
        files = self.getSubdir()

        # 处理返回结果，只需要目录名称
        r_files = [file.split(" ")[-1] for file in files]

        # 去除. ..
        return [file for file in r_files if file != "." and file !=".."]

    def getfiles(self, dirname=None):
        """返回文件列表，简要信息"""
        if dirname != None:
            self.cwd(dirname)  # 设置FTP当前操作的路径
        return self.nlst()  # 获取目录下的文件

    # 这个感觉有点乱，后面再说,
    # def getalldirs(self, dirname=None):
    #     """返回文件列表，获取整个ftp所有文件夹和文件名称简要信息"""
    #     if dirname != None:
    #         self.cwd(dirname)  # 设置FTP当前操作的路径
    #     files = []
    #     dirs = set(self.getdirs()) - set(self.getfiles())
    #     if dirs != {}:
    #         for name in dirs:
    #             self.cwd("..")  # 返回上级
    #             files += self.getalldirs(name)
    #     return files

def test():
    ftp = MyFTP()  # 实例化
    ftp.connect("192.168.17.189", 21)  # 连接
    ftp.login("fast", "fast*123")  # 登录

    # 获取第一层目录下的文件
    # lst =ftp.getdirs()
    # print(lst)
    # for name in lst:
    #     ftp.cwd("..")  # 返回上级
    #     names = ftp.getdirs(name)
    #     print(names)

    lst = ftp.getdirs()  # 返回目录下文件夹和文件列表
    print(lst)
    ftp.quit()  # 退出

if __name__ == '__main__':
    test()