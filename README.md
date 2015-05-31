# ip_range_tools

Tools for identifying traffic from data centers and discovering IP ranges that are assigned to data centers, cloud providers, etc.

## Getting a list of networks by hand

Let's say you have a data center/cloud provider IP address and you want to filter requests from the entire network belonging to that
hosting provider. For example, let's say you're getting a lot of requests from `119.81.81.123`. First, look into that IP address using
ipinfo.io:

  $ curl http://ipinfo.io/119.81.81.123
  {
    "ip": "119.81.81.123",
    "hostname": "119.81.81.123-static.reverse.softlayer.com",
    "city": "Singapore",
    "country": "SG",
    "loc": "1.2931,103.8558",
    "org": "AS36351 SoftLayer Technologies Inc."
  }

The company is SoftLayer, and this address is in AS36351 (that's an [Autonomous System](http://en.wikipedia.org/wiki/Autonomous_system_%28Internet%29)
number).  Next stop, the ARIN Whois search at [whois.arin.net](http://whois.arin.net/). If you search for the ASN, you'll get to
the page [http://whois.arin.net/rest/asn/AS36351/pft](http://whois.arin.net/rest/asn/AS36351/pft). On that page, you'll see the
organization handle for the organization that owns that ASN, which happens to be [SOFTL](http://whois.arin.net/rest/org/SOFTL.html). On that
page, there's a helpful related network links, which leads to [http://whois.arin.net/rest/org/SOFTL/nets](http://whois.arin.net/rest/org/SOFTL/nets).
There's the list of all of netblocks assigned to SoftLayer.

You can get an XML representation of this page if you use `curl`, as follows:

    curl http://whois.arin.net/rest/org/SOFTL/nets | xmlstarlet fo

I'm piping the output to XMLStarlet because the default formatting is very difficult to read.




