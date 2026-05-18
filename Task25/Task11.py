def f(x):
    duodells = set()

    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            duodells.add(i)
            duodells.add(x//i)

    if len(duodells) > 0:
        return max(duodells)+min(duodells)



for i in range(900000, 1000000):
    m = f(i)

    if str(m)[-3:] == "112":
        print(i, m)

