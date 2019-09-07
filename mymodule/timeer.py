import time
def Timer():
    return  time.time()


t1 = Timer()
print(t1)
time.sleep(5)
t2 = Timer()
print(t2)
t = t2 -t1
print("used  %s seconds"%int(t))


