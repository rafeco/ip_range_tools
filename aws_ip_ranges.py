#!/usr/bin/env python

"""
Downloads Amazon AWS IP Address Ranges and converts them to CSV

Documentation: http://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
"""

import cidr
import json
import subprocess
import sys

URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

def get_json(url):
    p = subprocess.Popen(['curl', URL], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    return out

def extract_ip_blocks(txt):
    cidrs = {}

    aws_json = json.loads(txt)

    aws_ip_ranges = aws_json['prefixes']

    for ip_range in aws_ip_ranges:
        cidr = ip_range['ip_prefix']
        name = "AWS %s %s" % (ip_range['service'], ip_range['region'])

        cidrs[cidr] = name

    return cidrs

def emit_csv(cidrs):
    csv = []

    for key in cidrs:
        (range_start, range_end) = cidr.cidr_to_range(key)
        csv.append("%s,%s,%s" % (range_start, range_end, cidrs[key]))

    return csv

def main():
    xml = get_json(URL)
    cidrs = extract_ip_blocks(xml)
    csv = emit_csv(cidrs)

    for line in csv:
        print line

if __name__ == '__main__':
    status = main()
    sys.exit(status)
