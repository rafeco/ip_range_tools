#!/usr/bin/env python

# imports
import fileinput
import subprocess
import sys
import xml.etree.ElementTree as ET

# constants
# exception classes
# interface functions
class IpInfo:
    def __init__(ip):
        self.ip = ip

# internal functions & classes
def get_whois_ip_info(ip):
    url = "http://whois.arin.net/rest/ip/%s" % (ip)

    p = subprocess.Popen(['curl', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()

    root = ET.fromstring(out)

    whois_info = dict(ip=ip, name='', handle='', customer_name='', parent_name='', start_ip='', end_ip='')

    ns = {'arin': 'http://www.arin.net/whoisrws/core/v1'}

    for e in root.findall("arin:orgRef", ns):
        whois_info['name'] = e.attrib['name']
        whois_info['handle'] = e.attrib['handle']

    for e in root.findall("arin:customerRef", ns):
        if whois_info['name'] == '':
            whois_info['name'] = e.attrib['name']
        else:
            whois_info['customer_name'] = e.attrib['name']

    for e in root.findall("arin:parentNetRef", ns):
        whois_info['parent_name'] = e.attrib['name']

    name_element = root.find("arin:name", ns)

    if name_element is not None and name_element.text == "GOOGLE-CLOUD":
        whois_info['name'] = 'Google Cloud'

    for netblock in root.findall("arin:netBlocks/arin:netBlock", ns):
        whois_info['start_ip'] = netblock.find("arin:startAddress", ns).text
        whois_info['end_ip'] = netblock.find("arin:endAddress", ns).text

    return whois_info

def main():
    ranges = {}

    for line in fileinput.input():
        (ip, count) = line.rstrip().split('|')
        whois_info = get_whois_ip_info(ip)

        range_csv = "%s,%s,%s,%s" % (whois_info['start_ip'], whois_info['end_ip'], whois_info['name'].replace(',', ''), whois_info['handle'])

        if range_csv in ranges:
            ranges[range_csv] = ranges[range_csv] + int(count)
        else:
            ranges[range_csv] = int(count)

    for key in ranges:
        print key + "," + str(ranges[key])

if __name__ == '__main__':
    status = main()
    sys.exit(status)
