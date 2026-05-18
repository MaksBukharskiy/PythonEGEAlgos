def f(x, y):
    if x > y or "28" in str(x): return 0
    if x == y: return 1

    return f(x+1, y) + f(x*2, y)

print(f(2, 10) * f(10, 34))