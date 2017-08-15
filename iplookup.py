#!/usr/bin/env python
from dns.resolver import query as resolve

def main():
    '''
    Running this module directly allows for passing a list or string of domains for finding IPs from A records and CNAMEs.
    Returns as a printed List.
    '''

    ## DOMAIN LIST
    domains = ["google.com", "example.com"]
    #domains = "google.com"

    print(iplookup(domains))


def iplookup(domains):
    '''
    This function is used to lookup all IP addresses assigned to a domain using DNS resolution.

    :param domains: single domain as a string, or multiple domains as a List type
    :return: Returns a List of IP Addresses from the domains supplied as Params
    '''
    # convert single string arg to single item list
    ip_list = []
    if isinstance(domains, str):
        domains = [domains]

    for domain in domains:
        try:
            answer = resolve(domain)
        except Exception as e:
            print("Error occured doing lookup for {}".format(domain))
            break
        ip_list += [ ip.to_text() for ip in answer if not ip == None ]
    return ip_list



if __name__ == "__main__":
    main()