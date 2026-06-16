def f(n, f):
    s = ''

    while n>0:
        s = str(n%f) + s
        n//=f

    return s

for n in range(1, 1000):
    n3 = f(n, 3)

    if n%3==0:
        n3= '1'+n3+"21"
    else:
        ost = f((n%3)*5, 3)
        n3+=ost

    r = int(n3, 3)

    if r<=1130 and n%2!=0:
        print(n)

