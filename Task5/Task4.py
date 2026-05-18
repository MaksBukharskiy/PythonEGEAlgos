for n in range(1, 1000):
    r = hex(n//2)[2:]

    if n % 4 != 0:
        r = "f" + r + "a0"
    else:
        r = "15" + r + "c"

    if int(r, 16) < 65536:
        print(n)
