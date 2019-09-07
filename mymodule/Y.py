
import os, linecache
from openpyxl import Workbook

wb = Workbook()
sheet0 = wb.create_sheet('test result', index=0)

path = 'C:\\T1' #input('please input folder path:')
filename = '#CAMLinuxCOM_2019-07-27.log' #input('please input filename:')
sfilename = '1' #input('please input savefilename:')
filepath = os.path.join(path, filename)
txtfile = open(filepath, 'r', encoding='utf-8')
txtfileStr = txtfile.readlines()
n = 0

for eachline in txtfileStr:
    n += 1
    if eachline.__contains__('VI PIPE STATUS'):
        V = []
        print("\n行号为: ",n)
        line1 = linecache.getline(filepath, n+4)
        value1 = line1[63:70]
        value1 = value1.replace(' ', '', 7)
        # value1 = value1.strip()
        print(value1)
        value1 = int(value1)
        # print(type(value1))
        print(value1)
        line2 = linecache.getline(filepath, n+6)
        value2 = line2[63:70]
        value2 = value2.replace(' ', '', 7)
        value2 = int(value2)
        print(value2)
        line3 = linecache.getline(filepath, n+8)
        value3 = line3[63:70]
        value3 = value3.replace(' ', '', 7)
        value3 = int(value3)
        print(value3)
        line4 = linecache.getline(filepath, n+10)
        value4 = line4[63:70]
        value4 = value4.replace(' ', '', 7)
        value4 = int(value4)
        print(value4)
        line5 = linecache.getline(filepath, n+12)
        value5 = line5[63:70]
        value5 = value5.replace(' ', '', 7)
        value5 = int(value5)
        print(value5)
        V.append(value1)
        V.append(value2)
        V.append(value3)
        V.append(value4)
        V.append(value5)
        # D = [V]
        sheet0.append(V)

        # line1 = txtfileStr[n+4]
        # print(line1)
        # line2 = txtfileStr[n+6]
        # print(line2)
        # line3 = txtfileStr[n+8]
        # print(line3)
        # line4 = txtfileStr[n+10]
        # print(line4)
        # line5 = txtfileStr[n+12]
        # print(line5)
        # value1 = line1[32:39]
        # value1 = value1.replace(' ', '', 7)
        # value1 = int(value1)
        # V.append(value1)
        # value2 = line1[32:39]
        # value2 = value2.replace(' ', '', 7)
        # value2 = int(value2)
        # V.append(value2)
        # value3 = line1[32:39]
        # value3 = value3.replace(' ', '', 7)
        # value3 = int(value3)
        # V.append(value3)
        # value4 = line1[32:39]
        # value4 = value4.replace(' ', '', 7)
        # value4 = int(value4)
        # V.append(value4)
        # value5 = line1[32:39]
        # value5 = value5.replace(' ', '', 7)
        # value5 = int(value5)
        # V.append(value5)
        # D = [V]
        # sheet0.append(D)
    else:
        pass

save_path = path + '\\' + sfilename + '.xlsx'
wb.save(save_path)
