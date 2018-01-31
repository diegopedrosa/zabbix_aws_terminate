from zabbix import zabbix

def lambda_handler(event, context):
    z = zabbix()
    return z.terminate('teste123')
from zabbix import zabbix
import json

def lambda_handler(event, context):
    z = zabbix()
    if 'action' in event:
        if event['action'] == 'update_description':
            return z.update_description(event['host'],event['description'])
        if event['action'] == 'terminate':
            return z.terminate(event['description'])
    if 'detail' in event:
            return z.terminate(event['detail']['instance-id'])

