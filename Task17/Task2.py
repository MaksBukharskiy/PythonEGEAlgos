f = open("2.txt")
s = [int(x) for x in f]
ary = sum(s)/len(s)
k = 0
answ = []

for i in (len(s) -1):
    x = s[i]
    y = s[i+1]

    if (x>ary or y>ary) and sum(x+y)/7== 0:
        k+=1
        ary += [x+y]

print(k, min(ary))
