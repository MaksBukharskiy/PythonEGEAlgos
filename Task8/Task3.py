from itertools import *

cnt = 0

for i in product("0123456", repeat=7):
    s = "".join(i)
    
    if s[0] not in "035" and not ("22" in s and "44" in s):
        cnt +=1

print(cnt)


