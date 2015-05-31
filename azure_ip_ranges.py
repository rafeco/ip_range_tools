#!/usr/bin/env python

"""Downloads Microsoft Azure netblocks and converts them to CSV"""

# imports
import cidr
import subprocess
import sys
import xml.etree.ElementTree as ET

URL = 'http://download.microsoft.com/download/0/1/8/018E208D-54F8-44CD-AA26-CD7BC9524A8C/PublicIPs_20150526.xml'

# exception classes
# interface functions
# classes
# internal functions & classes
def get_public_ip_xml():
    p = subprocess.Popen(['curl', URL], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()

    return out

def extract_ip_blocks(xml):
    root = ET.fromstring(xml)

    cidrs = {}

    for e in root.findall("Region"):
        region = e.attrib["Name"]

        for e in e.findall("IpRange"):
            subnet = e.attrib["Subnet"]
            cidrs[subnet] = "Microsoft Azure %s" % (region)

    return cidrs

def emit_csv(cidrs):
    csv = []

    for key in cidrs:
        (range_start, range_end) = cidr.cidr_to_range(key)
        csv.append("%s,%s,%s" % (range_start, range_end, cidrs[key]))

    return csv

def main():
    xml = get_public_ip_xml()
    cidrs = extract_ip_blocks(xml)
    csv = emit_csv(cidrs)

    for line in csv:
        print line

if __name__ == '__main__':
    status = main()
    sys.exit(status)
