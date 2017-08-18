# iplookup

A small python module which accepts a single domain as a string, or multiple domains as a list, and returns a list of associated IPs (from both A record and CNAMEs).

* For domains with multiple A records (RRDNS), all A record IPs are returned
* IPv6 AAAA records are currently _NOT_ returned.
* For domains which are CNAMEs, the IP of the CNAME is returned
* If you give it an IP, it will return the IP back (so mixed lists are OK too)

## Install Example
```
pip install iplookup
```

## Example usage
```
from iplookup import iplookup

print(iplookup(["google.com", "example.com"]))
print(iplookup("yahoo.com"))

```
