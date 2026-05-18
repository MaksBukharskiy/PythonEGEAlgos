from ipaddress import *

net = ip_network("95.24.20.25/255.255.252.0", 0)

k = 0
for ip in net.hosts():
    k+=1

print(k - 11)