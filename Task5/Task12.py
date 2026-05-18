def perevod(n, osn):
    s = ''
    while n > 0:
        ost = n%osn
        s = str(ost) + s
        n = n//osn

    return s


setik = []
for n in range(1, 1000):
    n3 = perevod(n, 3)
    sums = sum([int(x) for x in str(n3)])
    ans = sums*3

    if n%3==0:
        n3 = n3 + n3[-2:]

    else:
        n3 = n3 + perevod(ans, 3)

    r = int(n3, 3)
    setik.append(r)



perebor = min([x for x in setik if x%2!=0 and x>208])
print(perebor)



