from ipaddress import *

ipaddress = ip_address("220.128.112.142")

for mask in range(1, 33):
    network = ip_network(f'{ipaddress}/{mask}', 0)

    if ("220.128.96.0" in str(network)) and (network[0] < ipaddress < network[-1]):
        print(network.netmask)