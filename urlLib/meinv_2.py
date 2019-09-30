import re, urllib.request, os,time

opener = urllib.request.build_opener()
headers = ("User-Agent",
           "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")

homepage ="http://www.win4000.com/meitu.html"
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



# 存在当前路径下的这个文件夹下
dirMaker('girls2')

os.chdir('girls2')

# print(homedata)
secondPagePat = '<a href="(http://www.win4000.com/meinv.+?.html)">'
secondPageUrls = re.findall(secondPagePat,homedata)
print(len(secondPageUrls))

for secondUrl in secondPageUrls:
    # datas = urllib.request.urlopen(secondUrl).read().decode("utf-8", 'ignore')
    # print(datas)

    dataMain = ''
    # dataMain = getData(secondUrl)
    def getPic(url):
        global dataMain
        dataMain = urllib.request.urlopen(url).read().decode("utf-8", 'ignore')
        # print(dataMain)


        secondMainPic ='data-original="(http://pic1.win4000.com/pic/0/7d/.+?.jpg)"'
        secondMainPic ='" data-original="(http://pic1.win4000.com/pic/.*?.jpg)"'
        curPage =re.findall(secondMainPic,dataMain)
        # print("curPage",curPage)

        file = curPage[0][-11:]
        print(file)

        urllib.request.urlretrieve(curPage[0],file)

    getPic(secondUrl)

    def getthirdUrls(url):
        # dataMain = urllib.request.urlopen(url).read().decode("utf-8", 'ignore')

        otherlink = '<a href="(http://www.win4000.com/meinv\d+_\d+.html)"><img src='

        otherlinks = re.findall(otherlink, dataMain)

        # print(otherlinks)
        return otherlinks


    thirdUrls = getthirdUrls(secondUrl)

    for thirdUrl in thirdUrls:
        try:
            getPic(thirdUrl)
        except:
            print("下载异常")
        time.sleep(0.5)












