str1 = "[2019-07-27 00:00:15]        0        20             662               0       656         0"
str1 = "drwxr-xr-x  2 pi pi    4096 8月  22 22:57 frp_0.13.0_linux_arm"
listStr = str1.split(" ")
print(listStr)
while "" in listStr:
    listStr.remove("")
print(listStr)
print(listStr[2:5])
print(listStr[-1])


print("==================================")
listStr = str1.split("   ")
print(listStr)
while "" in listStr:
    listStr.remove("")
print(listStr)
print(listStr[2:5])
print(listStr[-1])
