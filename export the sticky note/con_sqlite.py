#导入sqllite3模块 
import sqlite3
import re


def write_info(info):
    with open('sqlite_res_final2.txt','a+',encoding='utf-8',errors='ignore') as f:
        f.write(info)
        f.close()


# 1.硬盘上创建连接 
con = sqlite3.connect('plum.sqlite')

# 获取cursor对象 
cur = con.cursor() 
# 执行sql创建表 
#sql = 'select text from Note'
sql = 'select * from Note' 

try:
    #reg = re.compile(r"^\\id=.*?\s(.*)")
    
    cur.execute(sql)
    person_all = cur.fetchall() 
    # print(person_all) 
    # 遍历
    #person_all = [("\\id=，)]
    #p = ("\\id=)
    #p[0] = "\\id=
    #print(person_all[0][0])
    
##    t = person_all[0][0]
##    resub = re.sub(r'(\\id=.*?\s)',"",t)
##    print(resub)
    
    for p in person_all:
        resub = re.sub(r'(\\id=.*?\s)',"",p[0])
        #print(resub)
        #print(reg.findall(p[0]))
        #write_info(p[0])
        #print(p[0])
        
    
        write_info(resub)
except Exception as e: 
    print(e) 
    print('创建表失败') 
finally: 
    # 关闭游标 
    cur.close() 
    # 关闭连接 
    con.close()
