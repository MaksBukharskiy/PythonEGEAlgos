def f(num, osn):
    if num == 0:
        return '0'

    s = ''

    while num:
        s = str(num%osn) + s
        num//=osn

    return(s)

for n in range(5, 10000):
    n5 = f(n, 5)
    if n%5==0:
        n5+=n5[-2:]

    else:
        ss = (n%5) * 7
        n5 += f(ss, 5)

    r = int(n5, 5)

    if r > 200:
        print(r)
        break


