import pyautogui
import time
import xlrd
import pyperclip


pyautogui.FAILSAFE = True # 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常


def mouseClick(clickTimes,lOrR,img,reTry):  #点击时间，左右键，图片名，重复次数
    if reTry == 1:
        while True:
            location = pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,0.1秒后重试")
            time.sleep(0.1)
    elif reTry == -1:
        while True:
            print('循环')
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            print(location)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


def mainWork(img):
    i = 1
    while i < sheet1.nrows: #如果i小于总行数
        cmdType = sheet1.row(i)[0]
        if cmdType.value == 7.0:
            reTry = 1
            imglis = (sheet1.row(i)[1].value).split(",")
            img = imglis[0]
            img2 = imglis[1]
            #reTry为空单次
            location = pyautogui.locateCenterOnScreen(img,confidence=0.9)   #定位起始位置
            print(location)
            pyautogui.moveTo(location.x,location.y) #移动到图片坐标
            destination = pyautogui.locateCenterOnScreen(img2,confidence=0.9)    #目标图片图片
            print(destination)
            if location is not None:
                pyautogui.dragTo(destination.x,destination.y, button='left',duration=0.5)   #拖拽到目标位置
                print('拖拽',img+"到"+img2)
            
            
            #reTry不为空多次
            
            if sheet1.row(i)[2].ctype == 2 and sheet1.row(i)[2].value != 0: #第3列第2行非空
                #ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
                reTry = sheet1.row(i)[2].value      #如果非空则赋值，回到循环小于等于i则退出循环
                for r in range(int(reTry),-1,-1):
                    location = pyautogui.locateCenterOnScreen(img,confidence=0.9)   #定位起始位置
                    print(location)
                    pyautogui.moveTo(location.x,location.y) #移动到图片坐标
                    destination = pyautogui.locateCenterOnScreen(img2,confidence=0.9)    #目标图片图片
                    print(destination)
                    if location is not None:
                        pyautogui.dragTo(destination.x,destination.y, button='left',duration=0.5)   #拖拽到目标位置
                        print('拖拽',img+"到"+img2)
                    time.sleep(1)
            i+=1
                    
                    


if __name__ == '__main__':
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    #通过索引获取表格sheet页
    sheet1 = wb.sheet_by_index(0)
    
    mainWork(sheet1)
