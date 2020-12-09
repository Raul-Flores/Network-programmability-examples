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
interface {{name}}
 description {{description}}
 ip address {{ip}} {{mask}}
"""

try:
    connection = ConnectHandler(**device1)
    comando = connection.send_command('show run | sec interface')
except Exception as unknown_error:
        print ('Error no identificado segun captura en el log es: \n ' + str(unknown_error))
parseo = ttp(data=comando, template=ttp_template)
parseo.parse()
json_data = json.loads(parseo.result(format='json')[0])
for x in range(0,7):
    print  (json_data[0][x]['name'])