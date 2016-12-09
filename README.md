Python API for [https://sslbl.abuse.ch/](https://sslbl.abuse.ch/)
========


Install requirements
========

```shell
pip install -r requirements.txt
```

Import the class:

```python
from sslblacklistAPI import SSLBlackList
```

Then, search for a specific domain:


```python
from sslblacklistAPI import SSLBlackList

# will fetch the list at https://sslbl.abuse.ch/
res = SSLBlackList(True).retrieve_results()
print res

# will fetch the info for this specific fingerprint
res = SSLBlackList(True).search('1f0eddff3174fe3ebcfa4c625fe9f619a58e282e')
print res
```

Usage
========


For the full list of blacklisted SSL certificates: 

```shell
$ python API_example.py
[{'common_name': u'Utoc0athav.ibm', 'sha1': u'92423f824a666d95b12e63a56efde3ccc1ae7fc7', 'listing_reason': u'Dridex C&C', 'listing_date': u'2016-12-09 10:26:24'}, {'common_name': u'Terootjars
ec.1Streheprtwiof.vuelos', 'sha1': u'435c84f8dbf9dfc192383813701bf1caf827fdbf', 'listing_reason': u'Dridex C&C', 'listing_date': u'2016-12-09 10:26:22'}, {'common_name': u'stonithehe.Odat3heo
ur.travelersinsurance', 'sha1': u'a3a7dc38b90f718d3b34ea0fc6bec39c8f2f7a8c', 'listing_reason': u'Dridex C&C', 'listing_date': u'2016-12-09 10:26:20'}, {'common_name': u'fleil42.com', 'sha1': 
u'37f5caec6916965a7f9c2a4d2622334ae5f14c3a', 'listing_reason': u'Chthonic C&C', 'listing_date': u'2016-12-07 10:19:50'}, {'common_name': u'suwenzna.com', 'sha1': u'7cfe275ceae4245c73e08763124
d17ccaa19bf44', 'listing_reason': u'Vawtrak C&C', 'listing_date': u'2016-12-07 10:07:12'}, {'common_name': u'www.__RANDOM_STR_.com/O=__RANDOM_STR_./C=US', 'sha1': u'c4d608de17a85769eda8b3aeb3
adea6a58f21107', 'listing_reason': u'Gootkit C&C', 'listing_date': u'2016-12-07 10:04:06'},  ....
```

What's returned is a list of elements such as this one: 
```json
{
    'common_name': u 'Utoc0athav.ibm',
    'sha1': u '92423f824a666d95b12e63a56efde3ccc1ae7fc7',
    'listing_reason': u 'Dridex C&C',
    'listing_date': u '2016-12-09 10:26:24'
}
```

And for a specific fingerprint:

```shell
$ python API_example.py 
{'ssl_certificate': {'status': u'Blacklisted (Reason: Vawtrak C&C, Listing date: 2016-11-21 09:08:05)', 'issuer_common_name': u'C=xx, L=Default City, O=Default Company Ltd', 'ssl_version': u'TLS 1.2', 'subject_common_name': u'C=xx, L=Default City, O=Default Company Ltd', 'fingerprint': u'1f0eddff3174fe3ebcfa4c625fe9f619a58e282e', 'subject': u'C=xx, L=Default City, O=Default Company Ltd', 'issuer': u'C=xx, L=Default City, O=Default Company Ltd'}, 'malware_binaries': [{'timestamp': u'2016-11-20 17:09:04', 'dstPort': u'443', 'dstIP': u'185.25.50.107', 'md5_checksum': u'd68905ba80c46ae0b1b9a868c23a6ac6'}, {'timestamp': u'2016-11-20 01:39:38', 'dstPort': u'443', 'dstIP': u'185.25.50.107', 'md5_checksum': u'c292c7cfbf630de9885d205c47a7ccfd'}]}
```

What's returned is this exact structure: 
```json
{
    'ssl_certificate': {
        'status': u 'Blacklisted (Reason: Vawtrak C&C, Listing date: 2016-11-21 09:08:05)',
        'issuer_common_name': u 'C=xx, L=Default City, O=Default Company Ltd',
        'ssl_version': u 'TLS 1.2',
        'subject_common_name': u 'C=xx, L=Default City, O=Default Company Ltd',
        'fingerprint': u '1f0eddff3174fe3ebcfa4c625fe9f619a58e282e',
        'subject': u 'C=xx, L=Default City, O=Default Company Ltd',
        'issuer': u 'C=xx, L=Default City, O=Default Company Ltd'
    },
    'malware_binaries': [{
        'timestamp': u '2016-11-20 17:09:04',
        'dstPort': u '443',
        'dstIP': u '185.25.50.107',
        'md5_checksum': u 'd68905ba80c46ae0b1b9a868c23a6ac6'
    }, {
        'timestamp': u '2016-11-20 01:39:38',
        'dstPort': u '443',
        'dstIP': u '185.25.50.107',
        'md5_checksum': u 'c292c7cfbf630de9885d205c47a7ccfd'
    }]
}
```

Contributing
=======

Feel free to open issues, contribute and submit your Pull Requests. Released under MIT License.
You can also ping me on Twitter ([@PaulWebSec](https://twitter.com/PaulWebSec))
