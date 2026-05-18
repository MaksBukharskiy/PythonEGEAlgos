def count_n(n):
    array = []
    while n:
        array = [n%27] + array
        n //= 27
    return array

n = 6*343**1156-5*49**1147+4*7**1153-875


n27 = count_n(n)
print(n27.count(1))
