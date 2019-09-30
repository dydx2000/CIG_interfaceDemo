from urllib import request
from bs4 import BeautifulSoup


def getHtmlCode(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/56.0.2924.87 Mobile Safari/537.36'
    }
    url1 = request.Request(url, headers=headers)
    page = request.urlopen(url1).read().decode()
    return page


def getImg(page):
    soup = BeautifulSoup(page, 'html.parser')  # 按照html格式解析页面
    book_list = soup.find(attrs={"id": "book"})  # 找到id为book的标签,这是包含所有书名信息的最底层标签
    book_list_name = book_list.find_all(attrs={"class": "title"})  # 获取id为book标签下class为title的标签
    for book_one in book_list_name:
        print(book_one.string)


url = 'http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book'
page = getHtmlCode(url)
getImg(page)