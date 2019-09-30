import re, urllib.request, os,time

# 1.这里填首页路径
homepage ="http://www.520mtw.com/xgmn/11.html"  # 可以替换 1,2,3 来下载其他页
homedata = urllib.request.urlopen(homepage).read().decode("utf-8",'ignore')
def getData(url):
    urllib.request.urlopen(url).read().decode("utf-8", 'ignore')

# 创建文件夹方法
def dirMaker(dir):
    dirs = os.listdir()
    if dir in dirs:
        return True
    else:
        os.mkdir(dir)
        return False

# 存在当前路径下的这个文件夹下----设置存放路径
dirMaker('girls3_011')

os.chdir('girls3_011')

secondPicHomeurl = "http://img2.bigla.net/"

# 2 这里填链接样式
secondPagePat = '<a href="(/pic/\d+.html)" title="'
secondPageUrls = re.findall(secondPagePat,homedata)

print(secondPageUrls)


for secondUrl in secondPageUrls:
    secondUrl = "http://www.520mtw.com" + secondUrl
    print(secondUrl)
    # time.sleep(10)

    # 设置 dataMain  为全局
    dataMain = '' #解析网页内容
    # dataMain = getData(secondUrl)

    # 获取当前页的图片方法
    def getPic(url):
        global dataMain
        dataMain = urllib.request.urlopen(url).read().decode("utf-8", 'ignore')
        # print(dataMain)

        #secondMainPic ="<img src='(/uploads/allimg/.*?\d+/\d+-[A-Za-z0-9]+.jpg)'" # 注意实际解析到是的双引号还是单引号
        secondMainPic ="<img src='.*?(/uploads/allimg/[A-Za-z0-9]+/[A-Za-z0-9]+-[A-Za-z0-9]+.jpg)'" # 注意实际解析到是的双引号还是单引号
        # "<img src="/uploads/allimg/c180807/153364952060040-16314.jpg" id="bigimg" onload="javascript:if(this.width>900)this.width=900" border="0" alt="【ADN-091】 希岛爱理番号ADN-091作品封面">"
        curPage =re.compile(secondMainPic).findall(dataMain)
        # print(len(curPage))

        # time.sleep(10)

        if len(curPage) < 1:
            return

        print("当前页图片相对路径: ",curPage)



        # curPage[0] = "http://www.520mtw.com" + curPage[0]  # 加上网站域名
        curPage[0] = secondPicHomeurl + curPage[0]  # 加上网站域名
        print(curPage[0])  #打印当前页图片的完整路径
        file = curPage[0][-11:]
        print("另存为:",file)

        try:
            urllib.request.urlretrieve(curPage[0],file)
        except:
            print("get error or retrieval incomplete.")


    getPic(secondUrl)



    def getthirdUrls(url):


        try:
            otherlink = "<a href='(\d+_\d+.html)'>"
            otherlinks = re.findall(otherlink, dataMain)
        except:
            print("其他页链接解析失败.")

        # print(otherlinks)
        return otherlinks

    # 解析完一页换页时休息一下.
    time.sleep(2)
    thirdUrls = getthirdUrls(secondUrl)


    print(thirdUrls)


    if len(thirdUrls)>0:
        for thirdUrl in thirdUrls:
            thirdUrl = "http://www.520mtw.com/pic/" + thirdUrl
            print(thirdUrl)

            try:
                getPic(thirdUrl)
                print()
            except:
                print("下载异常")
            time.sleep(0.5)












