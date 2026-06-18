from math import *

for l in range(100000, 0, -1):
    n = 10+52+1989
    i = ceil(log2(n))
    ser = ceil(l*i/8)

    if 836*ser <= 639*1024:
        print(l)
        break

