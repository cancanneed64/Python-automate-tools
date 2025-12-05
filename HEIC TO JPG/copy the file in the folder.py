import os
import shutil


# 循环读取HEIC格式照片，写入JPG
def recyle_convert(org_path, dst_path):         
    # 判断是不是目录
    if os.path.isdir(org_path):
        file_list = os.listdir(org_path)
        print(file_list)
        for idx, file in enumerate(file_list):
            sub_path = os.path.join(org_path, file)
            recyle_convert(sub_path, dst_path)
    # 判断是不是文件
    elif os.path.isfile(org_path):
        
        # 判断照片格式
        if org_path.lower().endswith('.jpg') or org_path.lower().endswith('.mov'):
        
            # 读取图片
            path, filename = os.path.split(org_path)
            name, ext = os.path.splitext(filename)
            file_path = os.path.join(dst_path, '%s.jpg' % name)
            print(file_path)
            shutil.move(org_path, dst_path)

            
    else:
        print(org_path + 'is error format!')
    pass


# 主函数入口
def main():
    # dst path
    dst_path = ''
    #dst_path = os.getcwd()
    if os.path.exists(dst_path) is False:
        os.makedirs(dst_path)
        pass
    # org path
    org_path = ''
    # convert
    recyle_convert(org_path, dst_path)
    pass



if __name__ == '__main__':
    main()
    pass
