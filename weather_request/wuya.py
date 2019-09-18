# coding:utf-8

import requests

'''r = requests.post(
    url='http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',
    data={'cityId': 438})
print(r.json())

print(r.text)

r = requests.get('http://www.bing.com')
print(u'HTTP状态码:', r.status_code)
print(u'请求的URL:', r.url)
# print(u'获取Headers:', r.headers)
for header_key, header_value in r.headers.items():
    print(header_key, ":", header_value)
# print(u'响应内容:', r.text)'''

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

'''r = requests.get('http://www.bing.com')
print(u'HTTP状态码:', r.status_code)
print(u'请求的URL:', r.url)
# print(u'获取Headers:', r.headers)
for header_key, header_value in r.headers.items():
    print(header_key, ":", header_value)
# print(u'响应内容:', r.text)'''
