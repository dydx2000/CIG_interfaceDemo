import os
import shutil

#列出当前目录下的文件和文件夹
filepath ="D:\\testhome"
dir = os.listdir(filepath)

newpath = "D:\\testhome\\copytest"

try:
    os.mkdir("D:\\testhome\\copytest")
except Exception as e:
    print(e)
    print("newpath exists.")

for i in dir:

    print(i)
    # if os.path.isdir(i):
    #     print("%s is a directory"%i)

    # i = filepath + "\\" + i
    full_filepath = os.path.join(filepath,i)

    if os.path.isdir(full_filepath):
        print("%s is a directory!"%i)
    if full_filepath != newpath:
        shutil.copy(full_filepath,newpath)

print("===================================\n")

# os.system("dir  d:\\testhome")
# os.system("tree d:\\")

'''
filepath="e:"
def gci(filepath):

    files = os.listdir(filepath)
    for fi in files:
       fi_d = os.path.join(filepath,fi)
       if os.path.isdir(fi_d):
           gci(fi_d)
       else:
          print(os.path.join(filepath,fi_d))

gci(filepath)
'''