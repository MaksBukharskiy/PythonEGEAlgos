for x in '0123456789abcde':
    z = int(f'97968{x}13', 15) + int(f'7{x}213', 15)

    if z % 14 == 0:
        print(z//14)