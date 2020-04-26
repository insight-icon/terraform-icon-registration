import sys
import requests
import json
import codecs
import subprocess
# import sys
# from pprint import pprint
# from subprocess import run, PIPE

class PRepChecker(object):

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
        payload = {
            "jsonrpc": "2.0",
            "id": 1234,
            "method": "icx_call",
            "params": {
                "to": "cx0000000000000000000000000000000000000000",
                "dataType": "call",
                "data": {
                    "method": "getPReps",
                    "params": {
                        "startRanking": "0x1",
                        "endRanking": "0xffff"
                    }
                }
            }
        }

        response = requests.post(url, json=payload).json()
        assert response["jsonrpc"]
        assert response["id"] == 1234
        return response

    def check_if_exists(self, network_name, address, p2pendpoint):
        response = self._get_preps(network_name)
        exists = False
        for i in range(0, len(response['result']['preps'])):
            if response['result']['preps'][i]['address'] == address:
                exists = True
                print("Wallet already exists")
            if response['result']['preps'][i]['p2pEndpoint'] == p2pendpoint:
                if response['result']['preps'][i]['address'] != address:
                    sys.exit('You are registering an IP address that is already registered to another prep. Exiting')
        return exists

    def prep_reg(self, network_name, keystore, register_json, password):
        url, nid = self._get_url(network_name)

        address = json.load(codecs.open(keystore, 'r', 'utf-8-sig'))['address']
        print(address)
        with open(register_json, 'r') as f:
            p2p_endpoint = json.load(f)['p2pEndpoint']
        print(p2p_endpoint)

        if not self.check_if_exists(network_name, address, p2p_endpoint):
            print("registering")
            command = 'yes | preptools registerPRep --prep-json %s -k %s -p %s -u %s -n %i' % (register_json, keystore, password, url, nid)
        else:
            print("updating")
            command = 'yes | preptools setPRep --prep-json %s -k %s -p %s -u %s -n %i' % (register_json, keystore, password, url, nid)

        print(command)

        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        if err:
            sys.exit(err)
        return output


if __name__ == "__main__":
    network_name = sys.argv[1]
    keystore_path = sys.argv[2]
    register_json = sys.argv[3]
    keystore_password = sys.argv[4]
    p = PRepChecker()
    p.prep_reg(network_name, keystore_path, register_json, keystore_password)