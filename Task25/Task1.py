set1 = set()
x = 16

for i in range(1, int(x**0.5+1)):
    if x%i == 0:
        set1.add(i)
        set1.add(x//i)

set2 = [x for x in set1]
print(set2[::-1])
print(set1)

