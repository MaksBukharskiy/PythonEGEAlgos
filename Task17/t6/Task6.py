f = open("1.txt")
a = [int(x) for x in f]
a35 = min(x for x in a if x > 0 and abs(x)%35==0)
answ = []

for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]

    if (x!=y) and abs(x - y) % a35 == 0:
        answ.append(x + y)

print(len(answ), max(answ))
#87 184328

