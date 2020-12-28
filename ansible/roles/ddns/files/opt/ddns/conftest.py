import pytest


@pytest.fixture(autouse=True, scope='class')
def test_domain_name():
    return 'example.com'

@pytest.fixture(autouse=True, scope='class')
def test_hostname():
    return 'minecraft'

@pytest.fixture(autouse=True, scope='class')
def test_fqdn_record():
    return '10.0.0.0'

@pytest.fixture(autouse=True, scope='class')
def test_value_list_hosted_zones_by_name():
    list_hosted_zones_by_name = {
        'ResponseMetadata': {
            'RequestId': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
            'HTTPStatusCode': 200,
            'HTTPHeaders': {
                'x-amzn-requestid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                'content-type': 'text/xml',
                'content-length': '793',
                'date': 'Thu, 24 Dec 2020 12:29:48 GMT'
            }, 
            'RetryAttempts': 0
        },
        'HostedZones': [
            {
                'Id': '/hostedzone/ZXXXXXXXXXXXXXXXXXX',
                'Name': 'example.com.',
                'CallerReference': 'Route53DomainName-xxxxxxxxxxx',
                'Config': {
                    'PrivateZone': False
                },
                'ResourceRecordSetCount': 3
            },
            {
                'Id': '/hostedzone/ZYYYYYYYYYYYYYY',
                'Name': 'example.work.',
                'CallerReference': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX',
                'Config': {
                    'PrivateZone': False
                },
                'ResourceRecordSetCount': 7
            }
        ], 
        'DNSName': 'example.com',
        'IsTruncated': False,
        'MaxItems': '100'
    }
    return list_hosted_zones_by_name

@pytest.fixture(autouse=True, scope='class')
def test_value_list_resource_record_sets():
    list_resource_record_sets = {
        'ResponseMetadata': {
            'RequestId': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
            'HTTPStatusCode': 200,
            'HTTPHeaders': {
                'x-amzn-requestid': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx',
                'content-type': 'text/xml',
                'content-length': '1098',
                'date': 'Thu, 24 Dec 2020 12:44:11 GMT'
            },
            'RetryAttempts': 0
        },
        'ResourceRecordSets': [
            {
                'Name': 'example.com.',
                'Type': 'NS',
                'TTL': 172800,
                'ResourceRecords': [
                    {
                        'Value': 'ns-329.awsdns-41.com.'
                    },
                    {
                        'Value': 'ns-1240.awsdns-27.org.'
                    },
                    {
                        'Value': 'ns-1651.awsdns-14.co.uk.'
                    },
                    {
                        'Value': 'ns-637.awsdns-15.net.'
                    }
                ]
            },
            {
                'Name': 'example.com.',
                'Type': 'SOA',
                'TTL': 900,
                'ResourceRecords': [
                    {
                        'Value': 'ns-329.awsdns-41.com. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400'
                    }
                ]
            },
                {
                    'Name': 'minecraft.example.com.',
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': '10.0.0.0'
                        }
                    ]
                }
        ],
        'IsTruncated': False,
        'MaxItems': '100'
    }
    return list_resource_record_sets
