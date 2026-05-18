for i in range(1, 10000):
    i2 = bin(i)[2:]

    if i%2==0:
        i2+="10"
    else:
        i2+="01"

    res = int(i2, 2)

    if res > 222:
        print(i)
        break