from math import *

def f(s1, s2, m):
    if s1+s2 <= 108: return m%2==0
    if m==0: return 0

    h = [f(s1-2, s2, m-1), f(s1, s2-2, m-1), f(ceil(s1/2), s2, m-1), f(s1, ceil(s2/2), m-1)]
    return any(h) if m%2!=0 else all(h)


print([s2 for s2 in range(49, 200) if not f(60, s2, 1) and f(60, s2, 3)])
print([s2 for s2 in range(49, 200) if not f(60, s2, 2) and f(60, s2, 4)])

#[103, 104, 159, 160]
#[99, 100, 101, 102, 157, 158, 193, 194, 195, 196]