from itertools import *

bank = []

x = product("КОСУФ", repeat=5)
k = 0

for s in x:
    k += 1
    s = ''.join(s)

    if "Ф" not in s and s.count('У') == 2:
        bank.append(k)

if bank:
    print(max(bank))