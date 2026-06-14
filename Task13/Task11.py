from ipaddress import *

network = ip_network("112.160.0.0/255.240.0.0", 0)

k=0
for x in network:
    x2 = bin(int(x))[2:]
    if str(x2).count("1")%5==0:
        k+=1

print(k)