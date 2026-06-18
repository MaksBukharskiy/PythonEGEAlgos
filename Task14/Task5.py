
for x in range(1, 2031):
    num = 6**260 + 6**160 + 6**60 - x

    k = 0

    while num > 0:
        if num%6==0:
            k+=1

        num//=6

    if k == 202:
        print(x)
        break

