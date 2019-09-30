import urllib.request
from bs4 import BeautifulSoup



opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')]
urllib.request.install_opener(opener)
# urllib.request.urlretrieve(URL, path)

def get_content(url):
    html = urllib.request.urlopen(url)

    content = html.read()
    content = urllib.request.urlopen(url).read().decode("utf-8",'ignore')
    f =open("nvpai.html",'w',encoding='utf-8')
    f.write(content)
    f.close()


    return content


def get_images(content):
    oSoup = BeautifulSoup(content,"html5lib")
    oSoup = BeautifulSoup(content,'html.parser')

    all_images = oSoup.find_all('img', class_="BDE_Image")

    x = 1
    for img in all_images:
        print(img['src'])
        image_name=img['src'][-10:]
        # image_name = "%s.jpg" % x

        urllib.request.urlretrieve(img['src'], image_name)
        x += 1


url = "http://tieba.baidu.com/p/6275000354?red_tag=q1497523013"

content = get_content(url)

get_images(content)