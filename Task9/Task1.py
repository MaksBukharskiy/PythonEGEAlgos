f = open("2A.txt")

cnt = 0

for s in f:
    a = [int(x) for x in s.split()]
    
    a1 = [x for x in a if a.count(x) == 1]
    a2 = [x for x in a if a.count(x) == 3]

    if len(a2) == 3 and len(a1) == 3:
        if sum(a2)**2 > sum(a1)**2:
            cnt += 1

print(cnt)