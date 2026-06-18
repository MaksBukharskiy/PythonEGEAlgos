from math import *

for i in range(1, 1000):
    symb = 261
    bit = ceil(log2(i))

    moshnost = ceil(bit*symb/8)

    if moshnost*252500 > 31*1024*1024:
        print(i)
        break
