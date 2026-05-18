numbers = [9, 16, 1, -5, 5, 4, 7, 42]
m1 = m2 = numbers[0]
for n in numbers:
    if n > m1:
        m2 = m1
        m1 = n
    elif n > m2:
        m2 = n
print(m2)