def find_delitel(integer):
    array = set()

    for i in range(2, int(integer**0.5)+1):
        if integer%i==0:
            array.add(i)
            array.add(integer//i)

    if len(array) == 0:
        return 0
    return min(array) + max(array)


count = 0
for x in range(800001, 801000):
    m = find_delitel(x)

    if str(m)[-1] == '4':
        count +=1
        if count == 6: break
        print(x, m)
