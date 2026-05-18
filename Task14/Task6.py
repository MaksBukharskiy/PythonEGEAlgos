for x in range(1, 1000):
    a = 27**7 - 3**11 + 36 - x
    sm = 0

    while a:
        sm+= a%3
        a = a//3

    if sm == 22:
        print(x)    
        break
