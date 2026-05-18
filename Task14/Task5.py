for x in (1,1000):
    a = 125**200 + 5**x + 74
    k = 0

    while a:
        if a % 5 == 4:
            k+=1
        a//=5

    if a==100:
        print(x)