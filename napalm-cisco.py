from napalm import get_network_driver
import pprint
import json
driver_ios = get_network_driver('ios')
commands = ['show ip route', 'show ip int brief']
device1 = driver_ios(hostname='ios-xe-mgmt-latest.cisco.com', username='developer', password='C1sco12345', optional_args = {'port': 8181})

devices = [device1]

for all_devices in devices:
    all_devices.open()
    print ("Interfaces en NAPALM structured format")
    print ("#"*100)
    interfaces = all_devices.get_interfaces()
    print (json.dumps(interfaces, sort_keys=True, indent=4))
    print ("#"*100)
    print ("Extraer  todas las  interfaces ")
    for x in  interfaces.keys():
    	print (x)