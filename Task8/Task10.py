from itertools import product

k=0
for x in product('0123456', repeat=6):
    s = ''.join(x)

    chet = [x for x in s if int(x)%2==0]
    nechet = [x for x in s if int(x)%2!=0]

    if s[0] != '0':
        if s[-1] not in '0123':
            if len(chet)==len(nechet):
                k+=1

print(k)