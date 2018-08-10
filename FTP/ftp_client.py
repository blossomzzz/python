# !/usr/bin/python3  
# coding: utf-8  


import ftplib
import os
import sys

# FTP服务器的IP、端口、账户、密码
host = "192.168.17.189"
port = 21  # not str
username = "fast"
password = "fast*123"

# remote和local是相对客户端的
homeDir = "D:/zhanghao/"
localDir = "E:/zhanghao/"


# 获取连接
def getConnect(host, port, username, password):
    """
    :param host: FTP ip
    :param port: FTP port
    :param username: FTP userName
    :param password: FTP password
    :return: ftp
    """
    print("FTP connection...")
    result = [1, ""]

    try:
        ftp = ftplib.FTP()
        # ftp.set_debuglevel(2)
        ftp.connect(host, port)
        ftp.login(username, password)

        result = [1, "connection success", ftp]

    except Exception as e:
        result = [-1, "connection fail, reason:{0}".format(e)]

    return result


# 下载文件
def download(ftp, remotePath, localAbsDir):
    result = [1, ""]

    try:
        remotePath = format(remotePath)
        localAbsDir = format(localAbsDir)

        remoteRel = ""
        if remotePath == "":
            remotePath =homeDir
        else:
            if remotePath.startswith(homeDir):
                remoteRel = remotePath.replace(homeDir, "/")
                remoteRel = format(remoteRel)
            else:
                remoteRel = remotePath

        if localAbsDir == "":
            localAbsDir =localDir
            localAbsDir = format(localAbsDir)

        remoteAbs = format(homeDir, remoteRel)  # 服务端文件或文件夹的绝对路径

        if os.path.isdir(remoteAbs):
            rs = downloadDir(ftp, remoteRel, localAbsDir)
        else:
            rs = downloadFile(ftp, remoteRel, localAbsDir)

        if rs[0] == -1:
            result[0] = -1
        result[1] = result[1] + "\n" + rs[1]
    except Exception as e:
        result = [-1, "download fail, reason:{0}".format(e)]

    return result


def runFTP(remotePath, localPath):
    result =getConnect(
        host=host,
        port=port,
        username=username,
        password=password
    )

    if result[0] != 1:
        print(result[1])
        sys.exit()
    else:
        print("connection success")

    ftp = result[2]

    result =download(
        ftp=ftp,
        remotePath=remotePath,
        localAbsDir=localPath
    )

    # result = ftp_client.upload(
    #     ftp=ftp,
    #     remoteRelDir=remotePath,
    #     localPath=localPath
    # )

    # ftp.quit()

    print("全部成功" if result[0] == 1 else "部分失败")
    print(result[1])
    sys.exit()


def main():
    remotePath =homeDir
    localPath = localDir
    runFTP(remotePath, localPath)

main()