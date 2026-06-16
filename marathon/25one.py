def finddel(n):
    mn = set()

    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            mn.add(i)
            mn.add(n//i)

    return mn

k=0
for x in range(1125001, 20000000):
    d = finddel(x)
    ans = []

    sevendel = [x for x in d if str(x)!="7" and str(x)[-1]=='7']

    if len(sevendel) >0:
        print(x, min(sevendel))
        k+=1

        if k==5:
            break


