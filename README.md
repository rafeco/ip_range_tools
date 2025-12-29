# ip_range_tools

**⚠️ ARCHIVED REPOSITORY ⚠️**

This repository is archived and no longer maintained. The scripts here are legacy Python 2 code from 2015-2016 and are outdated.

**For current solutions, please use:**
- Official cloud provider IP range files (see links below)
- Modern IP lookup APIs like [IPinfo.io](https://ipinfo.io/), [IPapi](https://ipapi.co/), or [ip-api.com](http://ip-api.com/)
- Purpose-built tools like [geoip2](https://github.com/maxmind/GeoIP2-python) or [iprange](https://github.com/firehol/iprange)

The information below is preserved for historical reference and to help you find current resources.

---

Tools for identifying traffic from data centers and discovering IP ranges that are assigned to data centers, cloud providers, etc.

## Official Cloud Provider IP Ranges

All major cloud providers publish their IP ranges. Here are the current official sources:

### AWS (Amazon Web Services)
- **Official JSON**: https://ip-ranges.amazonaws.com/ip-ranges.json
- **Documentation**: https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
- Includes IPv4 and IPv6 ranges, organized by service and region
- Updated automatically when ranges change

### Google Cloud Platform
- **JSON format**: https://www.gstatic.com/ipranges/cloud.json
- **DNS TXT records**: `dig TXT _cloud-netblocks.googleusercontent.com`
- **Documentation**: https://cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults
- Includes Google Cloud and Google services

### Microsoft Azure
- **Download page**: https://www.microsoft.com/en-us/download/details.aspx?id=56519
- **Documentation**: https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview
- JSON format, updated weekly, organized by region and service
- Also provides Service Tags for firewall rules

### Oracle Cloud Infrastructure (OCI)
- **JSON format**: https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json
- **Documentation**: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm

### Cloudflare
- **IPv4**: https://www.cloudflare.com/ips-v4
- **IPv6**: https://www.cloudflare.com/ips-v6
- **API**: https://api.cloudflare.com/client/v4/ips

### DigitalOcean
- **CSV format**: https://www.digitalocean.com/geo/google.csv
- Updated periodically

## Useful Third-Party Services

### IP Lookup and Analysis
- **IPinfo.io**: https://ipinfo.io/ - Free API for IP geolocation and ASN lookup
  ```bash
  curl https://ipinfo.io/8.8.8.8
  ```
- **IP2Location**: https://www.ip2location.com/ - IP geolocation database
- **AbuseIPDB**: https://www.abuseipdb.com/ - Check IP reputation and report abuse
- **BGPView**: https://bgpview.io/ - BGP and ASN lookup tool

### WHOIS Services
- **ARIN WHOIS**: https://whois.arin.net/ - North American IP registry
- **RIPE NCC**: https://apps.db.ripe.net/db-web-ui - European IP registry
- **APNIC**: https://wq.apnic.net/ - Asia-Pacific IP registry
- **LACNIC**: https://query.lacnic.net/ - Latin American IP registry
- **AFRINIC**: https://afrinic.net/whois - African IP registry

### Aggregated Lists
- **Spamhaus**: https://www.spamhaus.org/drop/ - Known hostile networks
- **FireHOL IP Lists**: https://github.com/firehol/blocklist-ipsets - Curated IP blocklists
- **Tor Exit Nodes**: https://check.torproject.org/exit-addresses

## Scripts in This Repository (DO NOT USE)

**These scripts are NOT recommended for production use.** They are legacy Python 2 code from 2015-2016 and may not work with current APIs.

- `aws_ip_ranges.py` - Downloads AWS IP ranges (outdated, use official JSON instead)
- `azure_ip_ranges.py` - Downloads Azure IP ranges (broken, hardcoded 2015 URL)
- `google_cloud_ip_ranges.py` - Uses DNS to get Google Cloud ranges (better to use official JSON)
- `find_bot_ipblocks.py` - Looks up IP ranges via ARIN WHOIS (use modern APIs instead)

**Instead:** Download the official IP range files directly from the links above, or use modern libraries like `requests` or `httpx` in Python 3 to fetch and parse the JSON files.

## Getting Network Ranges by Hand

If you have an IP address and want to find the entire network block:

1. **Look up the IP** using IPinfo.io:
   ```bash
   curl https://ipinfo.io/119.81.81.123
   ```

2. **Note the ASN** (Autonomous System Number) from the "org" field

3. **Query WHOIS** for the ASN to find all associated networks:
   - ARIN: https://whois.arin.net/
   - Search for the ASN (e.g., AS36351)
   - Find the organization handle
   - View all networks for that organization

4. **Alternative**: Use BGPView for ASN details:
   ```
   https://bgpview.io/asn/[ASN]
   ```




