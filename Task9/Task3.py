f = open("1")

k = 0
count = 0
for s in f:
    k+=1
    a = [int(x) for x in s.split()]
    b = sorted(a)

    if max(a) < sum(a) - max(a):
        if b[-1] + b[0] == b[1] + b[2]:
            print(k)

