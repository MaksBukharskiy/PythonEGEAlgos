from itertools import *

ctr = 0

for i in permutations("МАРИНА", 6):
    str = "".join(i)

    if str[0] not in "АИ":
        ctr+=1

print(ctr)