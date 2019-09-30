import re , urllib.request,os,time
opener =urllib.request.build_opener()
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener.addheaders=[headers]

time.sleep(10)

#网站主页
urlhead ="http://www.ylzzd.com/xgmn/"

# 创建文件夹方法
def dirMaker(dir):
    dirs = os.listdir()
    if dir in dirs:
        return True
    else:
        os.mkdir(dir)
        return False

# 存在当前路径下的这个文件夹下
dirMaker('girls')

os.chdir('girls')

# 爬取方法
def crawler(url,path):
    # opener.open()
    urllib.request.urlretrieve(url,path)

# 91-115页有图
for i in range (91,116):
    # print(i)
    # global urlhead

    # 创建页面列表
    urllist =[]
    urlreal = urlhead +str(i)+".html"
    urllist.append(urlreal)
    for j in range(2,20):
        urlrealinside = urlhead +str(i)+ "_"+str(j)+".html"

        urllist.append(urlrealinside)

    # 下载每页下的图
    for suburl in urllist:

        try:

            #读取网页
            # mainpage = urllib.request.urlopen("http://www.ylzzd.com/xgmn/110.html").read().decode('utf-8',"ignore")
            mainpage = urllib.request.urlopen(suburl).read().decode('utf-8',"ignore")

            print(len(mainpage))

            # 大图样式,匹配链接
            picPat = 'img class="petImg" src="(.*?.jpg)"'
            # <img class="petImg" src="/uploadfile/2017/1020/20171020011701591.jpg">
            urlhome = "http://www.ylzzd.com"

            #匹配图片
            pics = re.findall(picPat,mainpage)

            print(pics)
            # print(len(pics))

            for i in range(0, len(pics)):
                pics[i] = urlhome + pics[i]
                pathlocal = pics[i][-12:]

                crawler(pics[i],pathlocal)
        except:
            # print("链接不存在")
            break
