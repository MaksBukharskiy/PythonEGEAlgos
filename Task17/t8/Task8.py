f = open("67.txt")

a = [int(x) for x in f]
srint = sum(a)/len(a)
ans = []

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if (x>srint or y>srint) and (x+y)%7 == 0:
            ans.append(x+y)


print(len(ans), min(ans))




