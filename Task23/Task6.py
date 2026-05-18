def preob(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return preob(a+1, b) + preob(a*3, b) + preob(a**2, b)

print(preob(4, 93))