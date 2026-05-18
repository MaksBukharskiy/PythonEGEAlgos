def g(x):
    return abs(x)%100==21 and len(str(abs(x)))==5


f = open("7.txt")
a = [int(x) for x in f]
a21 = max(x for x in a if g(x))
ans = []


for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if (g(x) + g(y))==1 and (x*x + y*y >= a21**2):
        ans.append(x+y)

print(len(ans), max(ans))
