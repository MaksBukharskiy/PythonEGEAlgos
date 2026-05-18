f = open('9.txt')

a = [int(x) for x in f]
kol = [x for x in a if x%32==0]
ans = []

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if ("-" in str(x) or "-" in str(y)) and (x+y)<len(kol):
        ans.append(x+y)

print(len(ans), max(ans))

#4969 299


