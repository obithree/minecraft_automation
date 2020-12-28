import requests
import socket
import boto3
import argparse


class DynamicDNS:
    def __init__(self, domain_name, hostname):
        self.domain_name = domain_name
        self.fqdn_address = f'{hostname}.{domain_name}'
        self.global_ip = self._get_grobal_ip()
        fqdn_record_now = self._get_fqdn_record(self.fqdn_address)
        self.upsert_flag = True if self.global_ip == fqdn_record_now else False
        self.boto3_client = self.boto3_setup()

    @staticmethod
    def boto3_setup():
        boto3_client = boto3.client('route53')
        return boto3_client
        #self._session = boto3.Session()

    @staticmethod
    def _get_grobal_ip()-> str:
        try:
            res = requests.get('http://inet-ip.info/ip')
            print(f'global_ip is {res.text}')
        except:
            print('failed get_global_ip')
        return res.text

    @staticmethod
    def _get_fqdn_record(fqdn_address:str) -> str:
        try:
            fqdn_record = socket.gethostbyname(fqdn_address)
            print(f'get_fqdn_record is {fqdn_record}')
        except:
            print('failed get_fqdn_record')
        return fqdn_record

    @staticmethod
    def set_fqdn_record(boto3_client, domain_name:str, fqdn_address:str, global_ip:str):
        response_list_hosted_zones_by_name = boto3_client.list_hosted_zones_by_name(DNSName=domain_name)
        hostedzone_id = [s['Id'].split('/')[2] for s in response_list_hosted_zones_by_name['HostedZones'] if f'{domain_name}.' in s['Name']  ]
        #hostzone_name = boto3_client.list_resource_record_sets(HostedZoneId=hostedzone_id)['ResourceRecordSets'][2]['Name']
        params = {
            'HostedZoneId': hostedzone_id[0],
            'ChangeBatch': {
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': f'{fqdn_address}.',
                            'Type': 'A',
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': global_ip
                                }
                            ]
                        }
                    }
                ]
            }
        }
        print('test')
        boto3_client.change_resource_record_sets(**params)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('domain_name') 
    parser.add_argument('hostname') 
    args = parser.parse_args()
    domain_name = args.domain_name
    hostname = args.hostname
    ddns = DynamicDNS(domain_name, hostname)
    if ddns.upsert_flag:
        print('global_ip is not changed. upsert record.')
        ddns.set_fqdn_record(
            boto3_client=self.boto3_client,
            domain_name=ddns.domain_name,
            fqdn_address=ddns.fqdn_address,
            global_ip=ddns.global_ip
        )
    else:
        print('global_ip is not changed.')
    print('finish ddns.py')
