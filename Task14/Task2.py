string = (16**350 * (15 * 3 - 29)**4**7 + 1007)//63
cntr = 0

while string:
    if string % 4 == 1:
        cntr +=1

    string//=4

print(cntr)

