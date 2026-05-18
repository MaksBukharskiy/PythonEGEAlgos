f = open("2.txt")
ans = []
k=0

a = [int(x) for x in f]

for i in range(len(a)-1):
    x = a[i]
    y = a[i + 1]

    if (abs(x)%7==0 and abs(y)%17!=0) or (abs(x)%17!=0 and abs(y)%7==0):
        if abs(x) % 17 != 0 or abs(y) % 17 != 0:
            k+=1
            ans.append(x+y)

print(k)
print(min(ans))