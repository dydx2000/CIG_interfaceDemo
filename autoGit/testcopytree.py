import os
import shutil

'''
#列出当前目录下的文件和文件夹 D:\myworkspace\web\web-vehicle-center-vue
#源文件夹
vehiclePath ="D:\\myworkspace\\web\\web-vehicle-center-vue"
# dir = os.listdir(filepath)

#各模块主文件夹路径
portalPath = "D:\\myworkspace\\web\\web-portal-vue"
sysconfigPath = "D:\\myworkspace\\web\\web-sysconfig-center-vue"
messagePath = "D:\\myworkspace\\web\\web-message-center-vue"
equipPath = "D:\\myworkspace\\web\\web-equip-center-vue"
personalPath = "D:\\myworkspace\\web\\web-personal-center-vue"
safetyPath = "D:\\myworkspace\\web\\web-safety-center-vue"
visitorPath = "D:\\myworkspace\\web\\web-visitor-center-vue"
accountPath = "D:\\myworkspace\\web\\web-account-center-vue"
unifiedportaPath = "D:\\myworkspace\\web\\web-unifiedporta-vue"

#下级目录路径
assets = "\\src\\assets"
components = "\\src\\components"
icons = "\\src\\icons"
store = "\\src\\store"
styles = "\\src\\styles"
layout = "\\src\\views\\layout"
'''

# 1 覆盖 portal 模块

path1 = "e:\\test_copy"
path2 = "d:\\test_copy"


def copyfile(path1, path2):
    files = os.listdir(path1)  # 获取源路径文件列表

    for file in files:

        fullFile1 = os.path.join(path1, file)  # 用join方法自动生成路径
        # print(fullFile1)
        # os.chdir(fullFile1)

        if os.path.isdir(fullFile1):  # 判断是否文件夹

            fullFile2 = os.path.join(path2, file)

            # 在目标文件夹创建子文件夹
            try:
                os.mkdir(fullFile2)
            except Exception as e:
                # print("文件夹已存在")
                pass

            # 在子文件夹中递归复制
            try:
                copyfile(fullFile1, fullFile2)

            except:
                pass

        else:

            try:
                shutil.copy(fullFile1, path2)
                print("copying file '%s'  to  '%s' " % (fullFile1, path2))
            except Exception as e:
                print(e)
                print("copying file failed!")


copyfile(path1, path2)

# 利用 os.system 调用 windows命令 复制
# os.system("xcopy %s %s /s /Y"%(path1,path2))
# os.chdir(path2)
# print(os.getcwd())
# print(os.system("git pull"))
# copyfile(filepath)
# copytree(path1,path2)
