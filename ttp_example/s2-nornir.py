from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')
print (nr.inventory.hosts)
for name in nr.inventory.hosts:
    print (nr.inventory.hosts[name].keys())
def configure_ntp(task):
    ntp = task.run(send_configs, configs=['ntp server ' + str(task.host['ntp_server'])])
result = nr.run(task=configure_ntp)
print_result (result)
