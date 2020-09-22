import sys
import requests
import json
import codecs
import subprocess
import os
from pathlib import Path

from iconsdk.wallet.wallet import KeyWallet


import random

# import sys
# from pprint import pprint
# from subprocess import run, PIPE

class PRepChecker(object):

    def __init__(self,
                 network_name: str,
                 keystore: str,
                 register_json: str,
                 password: str,
                 operator_wallet_path: str = None,
                 operator_wallet_password: str = None,
                 ):

        self.network_name = network_name
        self.keystore = keystore
        self.register_json = register_json
        self.password = password
        self.operator_wallet_path = operator_wallet_path
        self.operator_wallet_password = operator_wallet_password

    @staticmethod
    def _get_url(network_name):
        if network_name not in ['mainnet', 'testnet']:
            return ValueError('Need to specify network_name -> either mainnet or testnet')
        if network_name == 'mainnet':
            url = "https://ctz.solidwallet.io/api/v3"
            nid = 1
        elif network_name == 'testnet':
            url = "https://zicon.net.solidwallet.io/api/v3"
            nid = 80
        else:
            return ValueError('Need to specify network_name -> either mainnet or testnet')
        return url, nid

    def _get_preps(self, network_name):
        url, nid = self._get_url(network_name)
        # Per https://github.com/icon-project/icon-rpc-server/issues/147
        # This call just checks if prep is regisered already
        payload = {
            "jsonrpc": "2.0",
            "id": 1234,
            "method": "icx_call",
            "params": {
                "to": "cx0000000000000000000000000000000000000000",
                "dataType": "call",
                "data": {
                    "method": "getPRep",
                    "params": {
                        "address": self.address
                    }
                }
            }
        }

        response = requests.post(url, json=payload).json()
        return response

    def check_if_exists(self, network_name, address, p2pendpoint):
        response = self._get_preps(network_name)
        if 'error' in response:
            # prep doesn't exist -> registering
            return False
        else:
            return True

        # Per https://github.com/icon-project/icon-rpc-server/issues/147
        # This call just checks if prep is regisered already
        # for i in range(0, len(response['result']['preps'])):
        #     if response['result']['preps'][i]['address'] == address:
        #         exists = True
        #         print("Wallet already exists")
        #     if response['result']['preps'][i]['p2pEndpoint'] == p2pendpoint:
        #         if response['result']['preps'][i]['address'] != address:
        #             sys.exit('You are registering an IP address that is already registered to another prep. Exiting')
        # return exists
    @staticmethod
    def _generate_random_password():
        import random
        import string

        special_chars = "%&'()*+,-./:;<=>?@["*2
        password = ''.join([random.choice(string.ascii_letters + string.digits + special_chars ) for _ in range(12)])
        print("The operator wallet password is: " + password)
        return password

    def create_operator_wallet(self):
        wallet_path = os.path.join(os.path.abspath(Path(self.keystore).parent),
                                   '-'.join(os.path.basename(self.keystore)), "-operator")

        if not self.operator_wallet_password:
            self.operator_wallet_password = self._generate_random_password()

        self.operator_wallet_path = wallet_path
        if os.path.exists(wallet_path):
            print("Operator wallet already exists at path : " + wallet_path)
        else:
            content = KeyWallet.create()
            content.store(self.operator_wallet_path, self.operator_wallet_password)

        self.operator_wallet_address = json.load(codecs.open(self.operator_wallet_path, 'r', 'utf-8-sig'))['address']

    def prep_reg(self):
        url, nid = self._get_url(self.network_name)

        if not self.operator_wallet_path:
            self.create_operator_wallet()

        self.address = json.load(codecs.open(self.keystore, 'r', 'utf-8-sig'))['address']
        with open(self.register_json, 'r') as f:
            p2p_endpoint = json.load(f)['p2pEndpoint']

        if not self.check_if_exists(self.network_name, self.address, p2p_endpoint):
            print("registering")
            command = 'yes | preptools registerPRep --node-address %s --prep-json %s -k %s -p %s -u %s -n %i' % (
            self.operator_wallet_address, self.register_json, self.keystore, self.password, url, nid)
        else:
            print("updating")
            command = 'yes | preptools setPRep --node-address %s --prep-json %s -k %s -p %s -u %s -n %i' % (
            self.operator_wallet_address, self.register_json, self.keystore, self.password, url, nid)

        p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
        (output, err) = p.communicate()
        print(output)


if __name__ == "__main__":
    network_name = sys.argv[1]
    keystore_path = sys.argv[2]
    register_json = sys.argv[3]
    keystore_password = sys.argv[4]
    p = PRepChecker(network_name, keystore_path, register_json, keystore_password)
    p.prep_reg()
