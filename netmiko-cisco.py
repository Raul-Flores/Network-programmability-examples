from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

device1 = {
'device_type': 'cisco_xr',
'ip': 'ios-xe-mgmt-latest.cisco.com',
'username': 'developer',
'password': 'C1sco12345',
'port': 8181
}

devices = [device1]
for all_devices in devices:
    try:
        connection = ConnectHandler(**all_devices)
    except (AuthenticationException):
        print ('Fallo de autenticacion en el dispositivo: ' )
    except (NetMikoTimeoutException):
        print ('Timeout (tiempo agotado) en el dispositivo: ' )
    except (EOFError):
        print ('Fin del archivo al intentar en el dispositivo ' )
    except (SSHException):
        print ('Error de SSH. Estas seguro que esta habilitado en el dispositivo? ' )
    except Exception as unknown_error:
        print ('Error no identificado segun captura en el log es: \n ' + str(unknown_error))
    comando = connection.send_command('show  int ')
    comando2 = connection.send_command('show ip int brief ')
    print ("Interfaces in raw text (cli) format")
    print ("#"*100)
    print (comando)
    print ("#"*100)
    print ("Extraer  todas las  interfaces ")
    for x in comando2.splitlines():
        if not 'Interface' in x:
           print (x.split()[0])
    print ("#"*100)


