import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import re

playlisturl = 'https://music.163.com/#/playlist?id=2923735400'
downloadUrl = 'http://music.163.com/song/media/outer/url?id=%s.mp3'

driver = webdriver.Chrome('chromedriver.exe')
driver.get(playlisturl)

driver.switch_to.frame('contentFrame')
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'lxml')

lines = soup.find("tbody").find_all('tr')
songs = soup.find("tbody").find_all('div', class_='ttc')
songList = []

for i in range(len(songs)):
    song = songs[i]
    line = lines[i]
    try:
        id_label = song.find('span', class_='txt').find('a')
        name_label = song.find('b')
        tds = line.find_all('td')
        singer_label = tds[3].find('div', class_='text')
        songList.append({"id": id_label.get('href').split('=')[1], "name": name_label.get('title'), "singer": singer_label.get('title')})
    except Exception:
        pass

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'),
                         ("Host", "music.163.com")]
urllib.request.install_opener(opener)
for song in songList:
    try:
        filename = 'E:/music/' + song['name'] + ' - ' + re.sub('\W+', '', song['singer']) + '.mp3'
        urllib.request.urlretrieve(downloadUrl % song['id'], filename)
        print(filename)
    except Exception:
        pass

print(songList)






