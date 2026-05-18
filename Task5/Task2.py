for n in range(1, 10000):
    r = bin(n)[2:]
    
    r+= str(r.count("1")%2)
    r+= str(r.count("1")%2)

    if int(r, 2) > 125:
        print(n)
        break

