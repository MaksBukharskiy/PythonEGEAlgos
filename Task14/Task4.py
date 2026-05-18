from string import printable

for x in printable[:23]:
    x1 = int(f'7{x}38596', 23)
    x2 = int(f'14{x}36', 23)
    x3 = int(f'61{x}7', 23)

    if (x1 + x2 + x3) % 22 == 0:
        print((x1 + x2 + x3)//22)