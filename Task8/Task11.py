from itertools import *

k=0
for x in product(set("дионисий"), repeat=6):
    s = "".join(x)

    if ("д" in s) and ("н" not in s) or ("н" in s) and ("д" not in s):
        if s[0]!=s[1] and s[1]!=s[2] and s[2]!=s[3] and s[3]!=s[4] and s[4]!=s[5]:
            k+=1

print(k)


