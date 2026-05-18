from ipaddress import *

ipadr = ip_address("115.12.69.38")

for mask in range(1, 33):
    network = ip_network(f'{ipadr}/{mask}', 0)
    if ('115.12.64.0' in str(network)) and (network[0] < ipadr < network[-1]):
        print(network)
        break
