string = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2 * 27**2024 - 6561

cntr = 0

while string:
    if string % 27 > 9:
        cntr += 1

    string //= 27

print(cntr)
