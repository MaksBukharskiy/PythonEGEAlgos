f = open("task2.txt")

listCntr = 0

for s in f:
    listCntr += 1

    a = [int(x) for x in s.split()]
    a2 = [x for x in a if a.count(x) == 3]
    a3 = [x for x in a if a.count(x) == 1]

    if len(a2) == 3 and len(2) == 3:
        if a2[0] > sum(a3)/3:
            print(listCntr)
            