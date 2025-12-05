import asyncio
#from win10toast import ToastNotifier
from pyppeteer import launch
import csv
import time



async def spamcheck(url,username,password):
    browser = await launch(headless = False, userDataDir = r'D:\Temp')
    page = await browser.newPage()
    path = 'D:\Temp'
    await page.goto(url)
    try:
        await page.type('#content > form > table:nth-child(4) > tbody > tr > td > dl > dd > table > tbody > tr:nth-child(1) > td > input[type=text]',username)
        await page.type('#content > form > table:nth-child(4) > tbody > tr > td > dl > dd > table > tbody > tr:nth-child(2) > td > input[type=password]:nth-child(2)',password)
        await page.click('#content > form > table:nth-child(4) > tbody > tr > td > dl > dd > div > table > tbody > tr > td > input')
    except Exception:
        print('Cannot login {}!'.format(username))
    else:
        print('Login {} Susccessfully!'.format(username))

    try:
        await page.waitForSelector('#process_selected1',options={'timeout': 5000})
    except Exception:
        print('No Spam Emails Found for {}!'.format(username))
    else:
        #ToastNotifier().show_toast("Spam Emails Found!!", username, icon_path=None, duration=None, threaded=True, callback_on_click=None)
        await page.screenshot({'path': path + '\\' + username + '_'+ time.strftime(r"%Y%m%d_%H%M")+'.png'})
        print("Screenshot saved for {}!".format(username))
        #await page.click('#yui-dt17-th-mid-liner')
        #await page.select('#message_action1','Release')
        #await page.click('#process_selected1')
        try:
            await page.waitForSelector('#confirm_ok',options={'timeout': 5000})   
        except Exception:
            print('Cannot Popup windows for {}!'.format(username))
        else:
            #print('Popup Succuss!')
            #await page.click('#confirm_ok')
            print("Successfully Release All Emails for {}!".format(username))

    #await asyncio.sleep(10)
    await page.close()
    await browser.close()


async def main():
    url = ''
    with open("rms1.csv", "r") as data:
        reader = csv.reader(data)
        next(reader)
        accounts = list(row for row in reader)
        tasks = list(spamcheck(url,account[0],account[1]) for account in accounts) 
    
    await asyncio.gather(*tasks)



asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.get_event_loop().run_until_complete(main())
#asyncio.run(main())

print("Now Time: "+time.strftime(r"%Y-%m-%d %H:%M"))
