from math import *

n = 17+4080
len = 257
i = ceil(log2(n))

alf = ceil(len*i/8)
all = (8388608*alf)/1024/1024

print(all)


