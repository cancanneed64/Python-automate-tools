import asyncio, time
from pyppeteer import launch
from win10toast import ToastNotifier




async def main(mod,webpage):
    browser = await launch(headless=mod, dumpio=True, autoClose=False,
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])   # 进入有头模式
    page_list = await browser.pages()
    #page = await browser.newPage()           # 打开新的标签页
    page = page_list[-1]

    await page.setViewport({'width': 1920, 'height': 1080})      # 页面大小一致
    await page.goto(webpage) # 访问主页

    # evaluate()是执行js的方法，js逆向时如果需要在浏览器环境下执行js代码的话可以利用这个方法
    # js为设置webdriver的值，防止网站检测
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    # await page.screenshot({'path': './1.jpg'})   # 截图保存路径

    #page_text = await page.content()   # 获取网页源码
    #print(page_text)
    #time.sleep(1)
    
    # 输入要查询的关键字，type第一个参数是元素的selector，第二个是要输入的关键字
    #await page.type('#kw', 'pyppeteer')
    # 点击提交按钮 click通过selector点击指定的元素
##    await page.click('#notify-content > form > div:nth-child(4) > div > input.btn.btn-success',
##                  options={'button': 'left', #left, right, of middle, defaults to left
##                           'clickCount': 1,   # 1 or 2
##                           'delay': 300,     # 毫秒
##                           })
    #等待元素出现
    #WR = await page.waitForSelector('#notify-content > form > div:nth-child(4) > div > input.btn.btn-success')
 
    
    while True:
        try:
            
            await page.click('#notify-content > form > div:nth-child(4) > div > input.btn.btn-success')
            print("have a page elem")
            print("click complete,waiting for next time")
        except:
            print("waiting")
            await asyncio.sleep(60)
            await page.reload()



    #await browser.close()
    
    #toaster = ToastNotifier()
    #toaster.show_toast("Tip",'Complete Click github!!!', threaded=False, icon_path=None, duration=100)


    
mod = False
webpage = 'https://github.com/'

asyncio.get_event_loop().run_until_complete(main(mod,webpage)) #调用
