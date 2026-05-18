from ipaddress import *

for mask in range(33):
    net = ip_network(f"145.192.94.230/{mask}", 0)

    if str(net.network_address) == "145.192.80.0":
        print(net.netmask)

print("answer: 240") 