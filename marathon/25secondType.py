def finddel(n):
    ans = set()

    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            ans.add(i)
            ans.add(n//i)

    return ans

k=0
for x in range(5400001, 6000000):
    dels = finddel(x)
    z = [f for f in dels if len(finddel(f))==2]

    if len(z)>0:
        m = max(z) + min(z)
        if m>60000 and str(m)==str(m)[::-1]:
            print(x, m)
            k+=1

            if k==5:break


