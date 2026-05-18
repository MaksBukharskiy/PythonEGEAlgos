from itertools import *

cntr = 0

for i in product("0123456", repeat=7):
    string = "".join(i)

    if string[0] not in "035" and not ("22" in string and "44" in string):
        cntr+=1

print(cntr)