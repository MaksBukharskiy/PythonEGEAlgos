from itertools import *

k = 0
for x in product(sorted('москва'), repeat=6):
    s = ''.join(x)
    k+=1

    if k%2==0 and s[0] not in 'авк' and s.count('к')==2 and 'кк' not in s:
            print(k)
            break


