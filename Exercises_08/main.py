from devices import Firewall
from devices import Switch 
from devices import LoadBalancers 


# Create a firewall instance 
firewall27 = Firewall("firewall27") 
# Configure it 
firewall27.configure_firewall() 
# Create a firewall instance 
firewall28 = Firewall("firewall28") 
# Verify a CRC 
crc = firewall28.calculate_crc("Dummy")
print("CRC : ",crc)

# Create a Switch instance 
switch01 = Switch("switch01") 
# Configure it 
switch01.configure_switch() 
# Create a firewall instance 
switch02 = Switch("switch02") 
# Verify a CRC 
bandwidth = switch02.calculate_bandwidth("Dummy")
print("Bandwidth : ",bandwidth)

# Create a LoadBalancer instance 
loadbalancer_01 = LoadBalancers("Dummy") 
# Configure it 
loadbalancer_01.configure_loadbalancer() 
# Create a LoadBalancer instance 
loadbalancer_02 = LoadBalancers("Dummy") 
# Get domain name 
domain_name = LoadBalancers.get_domain_name("Dummy")
print("Domain Name : ",domain_name)