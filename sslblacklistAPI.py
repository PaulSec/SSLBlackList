"""
This is the (unofficial) Python API for sslbl.abuse.ch Website.
Using this code, you can retrieve SSL certificates that have been blacklisted for malicious activities.

"""
from __future__ import print_function

import requests
import sys
import json

from bs4 import BeautifulSoup


class SSLBlackList(object):

    """SSLBlackList Main Handler"""

    def __init__(self, verbose=False):
        self.verbose = verbose

    def display_message(self, s):
        if self.verbose:
            print('[verbose] %s' % s)


    def extract_ssl_certificates(self, table):
        res = []
        trs = table.findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            data = {'listing_date': tds[0].text, 
                    'sha1': tds[1].find('a').contents[0],
                    'common_name': tds[2].text,
                    'listing_reason': tds[3].text}
            res.append(data)
        return res

    def extract_info_fingerprint(self, soup):
        res = {}
        table = soup.findAll('table', attrs={'class': 'tlstable'})[0]
        res['ssl_certificate'] = self.extract_ssl_certificate_information(table)
        table = soup.findAll('table', attrs={'class': 'sortable'})[0]
        res['malware_binaries'] = self.extract_associated_malware_binaries(table)

        return res

    def extract_ssl_certificate_information(self, table):
        trs = table.findAll('tr')
        tds = table.findAll('td')
        return  {'subject_common_name': tds[0].text,
                'subject': tds[1].text,
                'issuer_common_name': tds[2].text,
                'issuer': tds[3].text,
                'ssl_version': tds[4].text,
                'fingerprint': tds[5].text,
                'status': tds[6].text}


    def extract_associated_malware_binaries(self, table):
        res = []
        trs = table.findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            data = {'timestamp': tds[0].text,
                    'md5_checksum': tds[1].text,
                    'dstIP': tds[2].text,
                    'dstPort': tds[3].text}
            res.append(data)
        return res


    def retrieve_results(self):
        sslbl_url = 'https://sslbl.abuse.ch/'

        req = requests.get(sslbl_url)
        soup = BeautifulSoup(req.content, 'html.parser')

        if req.status_code != 200:
            print(
                u"Unexpected status code from {url}: {code}".format(
                    url=sslbl_url, code=req.status_code),
                file=sys.stderr,
            )
            return []

        soup = BeautifulSoup(req.content, 'html.parser')
        table = soup.findAll('table', attrs={'class': 'sortable'})[0]
        return json.dumps(self.extract_ssl_certificates(table))

    def search(self, sha1_fingerprint):
        url = "https://sslbl.abuse.ch/intel/{}".format(sha1_fingerprint)
        req = requests.get(url)

        if req.status_code != 200:
            print(
                u"Unexpected status code from {url}: {code}".format(
                    url=url, code=req.status_code),
                file=sys.stderr,
            )
            return {}

        soup = BeautifulSoup(req.content, 'html.parser')
        return json.dumps(self.extract_info_fingerprint(soup))
