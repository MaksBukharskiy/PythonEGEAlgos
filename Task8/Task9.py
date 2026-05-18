from itertools import *

k = 0
for i in product(sorted("компьютер"), repeat = 6):
    k+=1
    s = ''.join(i)

    if k%2 == 1:
        if (s[0] not in 'ь') and (s.count("к") == 2):
            print(k)

