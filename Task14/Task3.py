string = 30*36**231+18*6**101-3*36**45-2357
cntr = 0

while string:
    number = string%36

    if (number%5 == 0) + (number%3 == 0) == 1:
        cntr += 1

    string//=36

print(cntr)