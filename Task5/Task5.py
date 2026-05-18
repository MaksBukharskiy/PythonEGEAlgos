for n in range(1, 10000):

    r = bin(n)[2:]
    r2 = ""

    for i in r:
        if i == "1": r2 += "10"
        if i == "0": r2 += "01"

    if int(r2, 2) > 63:
        print(int(r2, 2))
        break