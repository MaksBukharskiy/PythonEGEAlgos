from itertools import *

k = 0
for i in product('ДГИАШЭ', repeat=5):
    a = ''.join(i)

    if (a[0] not in 'ИАЭ') and (a[-1] not in 'ДГШ'):
        k += 1

print(k)