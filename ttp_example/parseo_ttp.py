from netmiko import ConnectHandler
from pprint import pprint
from ttp import ttp
import json
device1 = {
'device_type': 'cisco_ios',
'ip': 'ios-xe-mgmt-latest.cisco.com',
'username': 'developer',
'password': 'C1sco12345',
'port': 22
}
ttp_template  = """
<group name="table_data"> 
{{intf_name}}   {{ ip }}    YES NVRAM  {{ status_pyh}} {{status_layer2 | _line_}} {{ protocol }} 
</group>
"""
try:
    connection = ConnectHandler(**device1)
    comando = connection.send_command('show ip int brief')
    print (comando)
except Exception as unknown_error:
        print ('Error no identificado segun captura en el log es: \n ' + str(unknown_error))
parseo = ttp(data=comando, template=ttp_template)
parseo.parse()
json_data = json.loads(parseo.result(format='json')[0])
pprint (json_data)