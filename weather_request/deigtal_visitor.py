# coding:utf-8

import requests
import json

# 登录请求头
headers = {'Content-Type': 'application/json;charset=UTF-8'}
cookie = ''


# 登录
def login():
    print("登录")

    global cookie
    body = {"loginName": "ironman", "password": "111111"}
    headers = {'content-type': "application/json"}

    r = requests.post(url='http://117.78.21.190/api/sysconfig/login', data=json.dumps(body), headers=headers)
    print(r.text)
    print()

    # for header_key, header_value in r.headers.items():
    #     print(header_key, ":", header_value)
    cookie = r.json()['data']
    # print(cookie)


token = cookie

# 获取黑名单列表

'''header_blacklist = {'Connection': 'keep-alive', 'Content-Length': '376', 'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json;charset=UTF-8', 'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Authorization': 'loginToken=' + cookie}'''


def get_blackList():
    print("获取黑名单")
    # 请求头
    header_blacklist = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': cookie}

    # 请求路径
    url = 'http://117.78.21.190/api/visitor/blackList/queryPageList/?pageNum=1&pageSize=10'

    # 请求
    r = requests.get(url=url, headers=header_blacklist)
    # print(u'HTTP状态码:', r.status_code)
    # print(u'请求的URL:', r.url)
    print(r.json())
    # for header_key, header_value in r.json().items():
    #     print(header_key, ":", header_value)

def get_whiteList():
    print("获取白名单")
    # 请求头
    header_blacklist = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': cookie}

    # 请求路径
    url = 'http://117.78.21.190/api/visitor/whitelist/queryPageList/?pageNum=1&pageSize=10'

    # 请求
    r = requests.get(url=url, headers=header_blacklist)
    # print(u'HTTP状态码:', r.status_code)
    # print(u'请求的URL:', r.url)
    print(r.json())
    # for header_key, header_value in r.json().items():
    #     print(header_key, ":", header_value)


if __name__ == '__main__':
    login()
    get_blackList()
    get_whiteList()
