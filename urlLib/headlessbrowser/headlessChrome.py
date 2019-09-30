from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re,urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'),
                     ("Referer", 'http://www.gaultier-x.com/xxxpost/98669.htm')]
urllib.request.install_opener(opener)


# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


# 驱动路径
# path = r'C:\Users\ZBLi\Desktop\1801\day05\ziliao\chromedriver.exe'

# 创建浏览器对象
# browser = webdriver.Chrome()
browser = webdriver.Chrome(chrome_options=chrome_options)

# 上网
url = 'http://www.gaultier-x.com/xxxpost/98621.htm'
url = 'http://www.gaultier-x.com/xxxpost/98661.htm'
url = 'http://www.gaultier-x.com/xxxpost/98669.htm'
url = 'http://www.gaultier-x.com/xxxpost/98660.htm'
url = 'http://www.gaultier-x.com/xxxpost/98772.htm'
url = 'http://www.gaultier-x.com/xxxpost/98764.htm'
# url = 'http://www.gaultier-x.com/xxxpost/98761.htm'

# url = 'http://www.qq.com'
browser.get(url)
browser.maximize_window()

# browser.save_screenshot('hyaku.png')
# selenium 获取网页页面高度
#
# body_width = browser.execute_script("return document.body.offsetWidth;")
# body_height = browser.execute_script("return document.body.offsetHeight;")
# print(browser.execute_script("return document.body.clientHeight"))
# print(body_width)
# print(body_height)
js_height = "return document.body.clientHeight"
js_height = "return document.body.scrollHeight"

height = browser.execute_script(js_height)  # 网页全文高度
# print(height)


def scroll_down():
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = browser.execute_script("return document.body.scrollHeight")
    last_height = browser.execute_script("return document.body.clientHeight")
    i =0
    # while True:
    #     i+=1
    #     # Scroll down to the bottom.
    #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # Wait to load the page.
    #     time.sleep(3)
    #
    #     # Calculate new scroll height and compare with last scroll height.
    #     # new_height = browser.execute_script("return document.body.clientHeight")
    #     new_height = browser.execute_script("return document.body.scrollHeight")
    #
    #     print("next scroll %s"%i)
    #
    #     browser.save_screenshot('hyaku_'+str(i)+".png")
    #
    #     if new_height == last_height:
    #
    #         break
    #
    #     last_height = new_height

'''
for i in range(2,100):   #也可以设置一个较大的数，一下到底

    print(i)
    curHeight = i*300
    height = browser.execute_script(js_height)
    print(height)
    print("current height:",curHeight)
    print("page height", height)
    js = "var q=document.body.scrollTop={}".format(i*300)  #javascript语句
    browser.execute_script(js)
    if curHeight > height:
        break
    time.sleep(1)
    print()
'''

# scroll_down()

html = browser.page_source.encode('utf-8',"ignore").decode()

'''
f = open("hyaku.html",'wt',encoding="utf-8")
f.write(browser.page_source.encode("utf-8", "ignore").decode()) # 忽略非法字符

f.close()
time.sleep(2)


f2 = open("hyaku.html","r",encoding='utf-8')



contents = f2.read()
'''


# print(contents)
# print(type(contents))
# print(contents)

# time.sleep(20)
picPat = 'data-src="(http://x.iprox.xyz/.+?.jpg)">'
# picPat = 'img class="xly xld" src="(http://x.iprox.xyz/.+?.jpg)">'
# data-src="http://x.iprox.xyz/img5.uploadhouse.com/fileuploads/23793/23793815408020f6e9b1a9b7ce54046e9071ebc2.jpg">
# urlhome = "http://www.ylzzd.com"
# <img class="xly xld" src="http://x.iprox.xyz/cdn.pornpics.com/pics1/2014-12-25/286395_12big.jpg">
# <img class="xly xld" src="http://x.iprox.xyz/cdn.pornpics.com/pics1/2014-12-25/286395_11big.jpg">
#匹配图片

pics = re.findall(picPat,html)
print(pics)

for picurl in pics:
    # picname = "./van3/"+picurl[-10:]
    picname = picurl[-10:]
    # print(picurl)
    #
    if "/"  in picname:
        picname=picname.replace("/","_")

    urllib.request.urlretrieve(picurl,"./van4/"+picname)
    print(picname,"downloaded.")



    '''
    data = urllib.request.urlopen(picurl).read()
    fx = open('./van/' + picname, 'wb')
    fx.write(data)
    fx.close()
    '''

time.sleep(5)

# mainpage = urllib.request.urlopen(suburl).read().decode('utf-8',"ignore")



# browser.quit()
