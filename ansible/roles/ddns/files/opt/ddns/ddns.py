import dataclasses
import requests
import socket
import boto3

#@dataclasses.dataclass(frozen=True)
class DynamicDNS:
    def __self__(self, fqdn_address):
        self.fqdn_address = fqdn_address
        self.global_ip = self._get_grobal_ip()
        fqdn_record_now = self._get_fqdn_record(self.fqdn_address)
        if self.global_ip == fqdn_record_now:
            set_fqdn_record(self.fqdn_address, self.global_ip)

    def boto3_setup():
        self._session = boto3.Session()

    @classmethod
    def _get_grobal_ip(cls)-> str:
        try:
            res = requests.get('http://inet-ip.info/ip')
            print(f'global_ip is {res.text}')
        except:
            print('failed get_global_ip')
        return res.text

    @classmethod
    def _get_fqdn_record(cls, fqdn_address:str) -> str:
        try:
            fqdn_record = socket.gethostbyname(fqdn_address)
            print(f'get_fqdn_record is {fqdn_record}')
        except:
            print('failed get_fqdn_record')
        return fqdn_record

    @classmethod
    def set_fqdn_record(cls, fqdn_address:str, global_ip:str):
        pass
        
if __name__ == '__main__':
    try:
        DynamicDNS
    except:
        pass
