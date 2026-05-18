rlist = []

for n in range(1, 10000):
    n2 = bin(n)[2:]

    if n2.count("1") % 2 == 0:
        n2 = "10" + n2[2:] + "0"
    else:
        n2 = "11" + n2[2:] + "1"

    result = int(n2, 2)

    if result > 50:
        rlist+=[n]

print(min(rlist))