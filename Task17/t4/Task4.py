f = open("4.txt")

s = [int(x) for x in f]
k32 = len([x for x in s if x%32 == 0])
ans = []

for i in range(len(s) - 1):
    x = s[i]
    y = s[i+1]

    if ("-" in str(x) or "-" in str(y)) and ((x+y) < k32):
        ans.append(x+y)

print(len(ans), max(ans))

print(s)