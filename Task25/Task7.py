def f(n):
    delitel = set()
    for x in (1, int(n**0.5) + 1):
        if n%x == 0:
            delitel.add(x)
            delitel.add(n//x)

    return delitel

for i in range(12365266, 12400000):
    leni = len(f(i))

    if leni == 5 and len(sum(i)) == 1:
        print(i, leni)

