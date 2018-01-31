import json, requests
import boto3, os
from base64 import b64decode


class zabbix():
    def __init__(self):
        self.url = os.environ['url']
        self.header = {'Content-Type': 'application/json-rpc'}
        self.__user = boto3.client('kms').decrypt(CiphertextBlob=b64decode(os.environ['username']))['Plaintext']
        self.__password = boto3.client('kms').decrypt(CiphertextBlob=b64decode(os.environ['password']))['Plaintext']
        self.__auth = self.authentication()

    def exec_call(self, data):
        return requests.post(url=self.url, data=data, headers=self.header)

    def authentication(self):
        data = json.dumps(
            {"jsonrpc": "2.0", "method": "user.login", "params": {"user": self.__user, "password": self.__password},
             "id": 1})
        return (json.loads(self.exec_call(data).text))['result']

    def get_hosts(self, host):
        data = json.dumps({"jsonrpc": "2.0", "method": "host.get", "params": {"filter": {
            "host": [host]}, "output": ["host", "hostid"]}, "id": 1, "auth": self.__auth})
        return (json.loads(self.exec_call(data).text))['result'][0]['hostid']

    def get_hosts_by_description(self, description):
        data = json.dumps({"jsonrpc": "2.0", "method": "host.get", "params": {"filter": {
            "description": description}, "output": ["host", "hostid", "description"]}, "id": 1, "auth": self.__auth})
        for d in json.loads(self.exec_call(data).text)['result']:
            if d['description'] == description:
                return (d['hostid'])

        return None

    def update_description(self, host, description):
        hostid = self.get_hosts(host)
        data = json.dumps(
            {"jsonrpc": "2.0", "method": "host.update", "params": {"hostid": hostid, "description": description},
             "auth": self.__auth, "id": 1})
        return self.exec_call(data).text

    def terminate(self, description):
        hostid = self.get_hosts_by_description(description)
        data = json.dumps({"jsonrpc": "2.0", "method": "host.delete", "params": [hostid], "auth": self.__auth, "id": 1})
        return self.exec_call(data).txt


