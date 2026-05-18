def perevod(x, osn):
    s = ''

    while x>0:
        ost = x%osn
        s = str(ost) + s

        x//=osn
    return s

print(perevod(1325, 3))





