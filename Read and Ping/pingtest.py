import os
import time
import re
import pandas as pd
import numpy as np


#读取csv文件转化为列表
def read_info(path):
    df = pd.read_csv(path)
    #ar = np.array(df)
    #lis = ar.tolist()
    lis= df.values.tolist()
    text = ["".join(l) for l in lis ]
    #print(text)
    return text

#取str符号"."中间段得字符座位文件名称保存
def find_filename(cmd,i):
    start = i.find(".",0) + 1
    end = i.find(".",start)
    name = cmd + i[start:end] 
    return name

#正则查找字符串作为文件名称保存
def re_filename(cmd,i):
    pattern = re.compile(r'(?<=\.)(.*)(?=\.)')
    name = cmd + pattern.findall(i)
    return name


#保存文件名称
def save_txt(info,name):
    with open('{}.txt'.format(name),'w+')as f:
        f.write(info)
        f.close()


if __name__ == '__main__':


    weblis = ["outlook.office365.com",
              "teams.microsoft.com"]
    web = ["outlook.office365.com"]

    
    path = '1.csv'
    text = read_info(path)
    cmd = 'ping '
    
    for i in text:
        p = os.popen(cmd + i)
        print(p.read())
        name = find_filename(cmd,i)
        print(name)
        save_txt(p.read(),name)
    

'''
>>> help(a[0].index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found, 
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.
    '''
