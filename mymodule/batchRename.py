import os
import shutil

path1 = "c:\\work2"

files =os.listdir(path1)
print(files)
i =0
for file in files:

    if file.endswith("jpg"): #找 jpg打头的文件
        print(file)

        #文件源路径
        src =  os.path.join(path1,file)

        #目标路径
        file_dst = "renamed_" + str(i) + ".jpg"
        dst = os.path.join(path1,file_dst)
        i += 1

        #重命名
        try:
            os.rename(src,dst)
        except:
            print("file exists")
    # if file.startswith("png"): #找png 打头的文件
    #     print(file)
    #
    #     # 文件源路径
    #     src = os.path.join(path1, file)
    #
    #     # 目标路径
    #     file_dst = file + ".png"
    #     dst = os.path.join(path1, file_dst)
    #
    #     # 重命名
    #     os.rename(src, dst)

