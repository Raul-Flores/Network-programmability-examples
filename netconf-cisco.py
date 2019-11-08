from ncclient import manager
from xml.dom import minidom
import xmltodict

huaweiautomation = {'address':'ios-xe-mgmt-latest.cisco.com',
'netconf_port':  10000, 'username': 'developer', 'password': 'C1sco12345'}

huawei_manager = manager.connect(host = huaweiautomation["address"], port = huaweiautomation["netconf_port"], username = huaweiautomation["username"],
password = huaweiautomation["password"], device_params = {'name': 'iosxe'}, hostkey_verify = False)

filter_Interfaces= """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface>
  </interface>
 </interfaces>
</filter>
"""

#Para cualquier interfaz
huawei_get_interfaces = huawei_manager.get_config('running', filter_Interfaces).xml

xml_pretty = minidom.parseString(huawei_get_interfaces)
print ("Interfaces en XML format")
print ("#"*100)
print (xml_pretty.toprettyxml(indent="    "))

xml_to_dict_general = xmltodict.parse(huawei_get_interfaces)


print ("#"*100)
print ("Extraer  todas las  interfaces ")
for x in xml_to_dict_general['rpc-reply']['data']['interfaces']['interface']:
	print (x['name'])
print ("#"*100)


#print ("Estatus....")
#print ("")
#huawei_manager.connected
#Verificar capabilitys
#for capability in huawei_manager.server_capabilities:
#    print (capability)