import os
import time
import shutil

'''
import rarfile
import zipfile
import tarfile
import gzip



def un_rar(file_name):
    """unrar zip file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    if os.chdir(file_name + "_files"):
        rar.extractall()
    rar.close()

def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()

def un_tar(file_name):
    
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    #因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()

def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    open(f_name, "w+").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    #关闭gzip对象

'''


def diyun_zip(file_name,root):
    if os.path.splitext(file_name)[1] == ".zip":
        shutil.unpack_archive(root+'\\'+file_name)


path = ''
file_list = os.listdir(path)
release_path = ''
os.chdir(release_path)

    
for root, dirs, files in os.walk(path):
    #print(files)
    for i in files:
        ##print(i)
        diy_un_zip(i,root)

