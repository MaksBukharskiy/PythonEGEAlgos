from ipaddress import *

comp = ip_address("111.81.208.27")
for mask in range(1, 33):
    network = ip_network(f'{comp}/{mask}', 0)
    if ("111.81.192.0" in str(network)) and (network[0] < comp < network[-1]):
        print(network.netmask)