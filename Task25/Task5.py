
def dels(x):
    array = set()

    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            array.add(i)
            array.add(x//i)

    if len(array) == 0:
        return 0

    return sum(array)

cnt = 0
for x in range(500_001, 600_001):
    m = dels(x)

    if str(m)[-1] == "9" and cnt <= 4:
        print(x, m)
        cnt+=1


