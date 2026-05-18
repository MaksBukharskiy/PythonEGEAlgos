def dels_solution(x):
    set1 = set()

    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            set1.add(i)
            set1.add(x//i)

    if len(set1) == 0:
        return 0

    return min(set1) + max(set1)

cnt = 0
for x in range(900_001, 1000_000):
    m = dels_solution(x)

    if str(m)[-3:] == "112" and cnt <= 4:
        cnt+=1
        print(x, m)




