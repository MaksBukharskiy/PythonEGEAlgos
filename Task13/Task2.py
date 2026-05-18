from ipaddress import ip_network

net = ip_network("5.2.5.0/255.255.0.0", 0)
k = 0

for ip in net:
    ip_binary = bin(int(ip))[2:].zfill(32)

    if ip_binary.count('0') % 25 == 0:
        k+=1

print(k)