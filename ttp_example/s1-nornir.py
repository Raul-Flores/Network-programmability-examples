from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')

send_command = nr.run(task=netmiko_send_command, command_string="show ip int brief")
print_result (send_command)

