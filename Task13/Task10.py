from ipaddress import *

for i in range(1, 33):
    ip = ip_network(f'84.23.84.23/{i}', 0)

    if "84.23.84.0" in str(ip.network_address):
        print(ip.netmask)