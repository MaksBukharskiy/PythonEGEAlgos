def dels(n):
    mn = set()

    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            mn.add(i)
            mn.add(n//i)

    return mn



for x in range(190201, 190281):
    d = dels(x)
    d2 = [x for x in d if x%2==0]

    if len(d2)==4:
        print(sorted(d2)[::-1])

