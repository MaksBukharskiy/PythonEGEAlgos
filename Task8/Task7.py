from itertools import *

k = 0
for i in product("ОПРТ", repeat = 5):
    s = ''.join(i)
    k+=1

    if "ТОПОР" in s:
        print(k)
    if "РОПОТ" in s:
        print(k)


print(87 + 69 + 100)
