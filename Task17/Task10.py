f = open("somethin.txt")
a = [int(x) for x in f]
min123 = min([x for x in a if x>0 and x%123==0])

paircount = []

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if (x+y)<min123:
        paircount.append(x+y)

print(len(paircount), abs(max(paircount)))




