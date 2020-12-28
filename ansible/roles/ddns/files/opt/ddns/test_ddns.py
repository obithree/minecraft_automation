import pytest
from unittest import mock
from ddns import DynamicDNS

class TestDynamicDNS:

    def test_boto3_setup(self):
        pass

    def test_get_grobal_ip(self, test_fqdn_record):
        test_global_ip = DynamicDNS._get_grobal_ip()
        assert test_global_ip == test_fqdn_record

    def test_get_fqdn_record(self, test_domain_name, test_hostname, test_fqdn_record):
        test_fqdn_address = f'{test_hostname}.{test_domain_name}'
        test_fqdn_record = DynamicDNS._get_fqdn_record(test_fqdn_address)
        assert test_fqdn_record == test_fqdn_record

    def test_set_fqdn_record(self, test_domain_name, test_hostname, test_fqdn_record, test_value_list_hosted_zones_by_name, test_value_list_resource_record_sets):
        test_fqdn_address = f'{test_hostname}.{test_domain_name}'
        test_hostzone_id = test_value_list_hosted_zones_by_name['HostedZones'][0]['Id'].split('/')[2]
        params = {
            'HostedZoneId': test_hostzone_id,
            'ChangeBatch': {
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': f'{test_fqdn_address}.',
                            'Type': 'A',
                            'TTL': 300,
                            'ResourceRecords': [
                                {
                                    'Value': test_fqdn_record
                                }
                            ]
                        }
                    }
                ]
            }
        }
        with mock.patch('boto3.client') as boto3_client:
            boto3_client().list_hosted_zones_by_name.return_value = test_value_list_hosted_zones_by_name
            boto3_client().list_resource_record_sets.return_value = test_value_list_resource_record_sets
            ddns = DynamicDNS(test_domain_name, test_hostname)
            assert ddns.upsert_flag
            ddns.set_fqdn_record(ddns.boto3_client, test_domain_name, test_fqdn_address,test_fqdn_record)
            boto3_client().list_hosted_zones_by_name.assert_called_with(DNSName=test_domain_name)
            #boto3_client().list_resource_record_sets.assert_called_with(HostedZoneId=test_hostzone_id)
            boto3_client().change_resource_record_sets.assert_called_with(**params)
