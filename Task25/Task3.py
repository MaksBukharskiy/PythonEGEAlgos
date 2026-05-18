def find_del(x):
    set1 = set()

    for g in range(1, int(x**0.5)+1):
        if i%g==0:
            set1.add(g)
            set1.add(x//g)

    return set1

for i in range(190201, 190280+1):
    m = find_del(i)

    m2 = [i for i in m if i% 2 == 0]
    if len(m2) == 4:
        print(sorted(m2))