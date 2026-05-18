def f(n):
    uniqueDel = set()
    for d in range(2, int( n ** 0.5 ) + 1):
        if n % d == 0:
            uniqueDel.add(d)
            uniqueDel.add(n//d)

    return uniqueDel

