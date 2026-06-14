from itertools import *

k = 0
for x in product("авнрья", repeat=5):
    x = ''.join(x)
    k+=1

    if x[0]!='я' and x.count("ь")<=1 and 'яя' not in x:
        print(k)




