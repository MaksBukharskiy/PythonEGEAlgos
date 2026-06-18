from math import ceil, log2

from marathon import *

for x in range(1000, 0, -1):
    n = 10+52+458
    i = ceil(log2(n))

    numberweight = ceil(i*x/8)

    if numberweight * 862 <= 276 * 1024:
        print(x)
        break