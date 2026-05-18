def f(n):
    deliteli = set()
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            deliteli.add(x)
            deliteli.add(n//x)

    return deliteli

for i in range (500000, 501000):
    a = f(i)

    if len(a) > 0:
        r = sum(a)
        if str(r)[-1] == "9":
            print(i, r)
