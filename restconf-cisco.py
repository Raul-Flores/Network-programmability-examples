import requests
import urllib3
import json
from pprint import pprint
urllib3.disable_warnings()

user = 'developer'
password = 'C1sco12345'
host = 'ios-xe-mgmt-latest.cisco.com'

https_request_native = 'https://' + host +':9443'+'/restconf/data/Cisco-IOS-XE-native:native/interface/'
https_request_ietf = 'https://' + host +':9443'+'/restconf/data/ietf-interfaces:interfaces'

headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
response = requests.get(https_request_ietf, auth=(user, password), headers=headers, verify=False)

print ("Interfaces en json format")
print ("#"*100)
print (response.text)

interface = response.json()['ietf-interfaces:interfaces']['interface']
print ("#"*100)
print ("Extraer  todas las  interfaces ")
for x in interface:
	print (x['name'])
print ("#"*100)




#	for y in x['ietf-ip:ipv4'].values():
#		print ('direccion ip: '+ y[0]['ip'])


#print (interface[2]['ietf-ip:ipv4']['address'][0]['ip'])
#print (type(response.json()))

#Guardar la respuesta
#if response.status_code == 200:
#	content = response.text
#	file = open('interfaces.txt', 'w')
#	file.write(content)
#	file.close
#print (r.json)
#print (r.content)