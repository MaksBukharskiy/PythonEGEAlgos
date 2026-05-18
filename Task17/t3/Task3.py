f = open("3.txt")

s = [int(x) for x in f]
ary = sum(s)/len(s)
answ = []

for i in range(len(s)-1):
    x = s[i]
    y = s[i+1]

    if (x > ary or y > ary) and ((x+y) % 7 == 0):
        answ.append(x+y)

print(len(answ), min(answ))