from ipaddress import ip_network

net = ip_network('112.160.0.0/255.240.0.0', 0)
k = 0

for ip in net:
    binary_ip = bin(int(ip))[2:].zfill(32)

    if binary_ip.count('1') % 5 == 0:
        k+=1

print(k)
