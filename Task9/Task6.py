f = open("1")

k=0
for s in f:
    x = [int(x) for x in s.split()]
    z = sorted(x)
    k+=1

    if len(x) == len(set(x)):
        if (z[0]+z[-1])*2 == (z[1] + z[2] + z[3]) * 3:
            print(k)
