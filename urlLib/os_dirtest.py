import os

def dirExists(dir):
    dirs = os.listdir()
    if dir in dirs:
        print("true")
    else:
        print("false")
        os.mkdir(dir)

# dirExists('boys')

# path1 = "c:\\work2"

dirExists("testPath")
testPath ="testPath"

print(os.getcwd())
os.chdir(testPath)
print(os.getcwd())
print(os.listdir("../"+testPath))
print(os.listdir())
# os.system("dir")
print(os.walk(testPath))
