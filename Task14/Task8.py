for i in range(1, 2000+1):
    z = 3 ** 100 - i
    s = []

    while z:
        if z%3 == 0:
            s = [z%3] + s
        z//=3

    if s.count(0) == 2:
        print(i)
        break

