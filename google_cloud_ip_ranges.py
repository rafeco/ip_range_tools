#!/usr/bin/env python

"""
Downloads Amazon AWS netblocks and converts them to CSV.

Documentation at: https://cloud.google.com/compute/docs/faq#ipranges
"""

import cidr
import json
import subprocess
import sys

URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'

def dig_google(host):
    cmd = ['dig', '-t', 'TXT', host, '8.8.8.8', '+short']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = p.communicate()
    return out

def get_cidrs_from(host):
    response = dig_google(host)

    parts = response[1:-1].split()

    cidrs = []

    for p in parts:
        if p.startswith("ip4:"):
            c = p.replace("ip4:", "", 1)
            cidrs.append(c)

    return cidrs

def get_all_cidrs():
    out = dig_google('_cloud-netblocks.googleusercontent.com')

    parts = out[1:-1].split()

    cidrs = []

    for p in parts:
        if p.startswith("include:"):
            host = p.replace("include:", "", 1)
            cidrs = cidrs + get_cidrs_from(host)

    return cidrs

def emit_csv(cidrs):
    csv = []

    for c in cidrs:
        (range_start, range_end) = cidr.cidr_to_range(c)
        csv.append("%s,%s,%s" % (range_start, range_end, "Google Cloud"))

    return csv

def main():
    cidrs = get_all_cidrs()
    csv = emit_csv(cidrs)

    for line in csv:
        print line

if __name__ == '__main__':
    status = main()
    sys.exit(status)
