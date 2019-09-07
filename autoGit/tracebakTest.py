import traceback
try:
    1/0
except Exception as e:
    print(e)


try:
    1 / 0
except Exception as e:
    # traceback.print_exc()
    traceback.print_exc(file=open('tb.txt', 'w+'))
    list1 = traceback.format_exc()
    print(list1)
    print(list1[:10])
    # list2 = list1.capitalize(False)
    str1 = str(list1)
    print(str1)
    str1.upper()
    print(str1)

