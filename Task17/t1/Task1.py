f = open("1.txt")

arr = [int(x) for x in f]
ans = []

for i in range(len(arr)-1):
    x = arr[i]
    y = arr[i+1]

    if abs(x)%10==7 or abs(y)%10==7:
        ans.append(x+y)
        
print(len(ans), max(ans))