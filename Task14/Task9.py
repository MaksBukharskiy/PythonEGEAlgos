from string import printable

for i in printable[:29]:
    s1 = int(f'923{i}874', 29)
    s2 = int(f'524{i}6152', 29)

    if (s1 + s2) % 28 == 0:
        print(i, (s1+s2)//28)
