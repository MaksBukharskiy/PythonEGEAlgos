from itertools import *

x = product('ENO', repeat=5)
k = 0

for s in x:
    k+=1
    s = ''.join(s)
    if k == 32:
        print(k, s)         