a = open("1.txt")

k = 0
for s in a:
    x = [int(x) for x in s.split()]
    k+=1

    a3 = [a for a in x if x.count(a) == 3]
    a1 = [a for a in x if x.count(a) == 1]

    if len(a3) == 3 and len(a1) == 3:
        if (a3[0]) > (sum(a1)/len(a1)):
            print(k)


