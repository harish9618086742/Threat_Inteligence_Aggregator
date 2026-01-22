import re
import ipaddress

IP_RE = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
HASH_RE = r"\b[a-fA-F0-9]{32,64}\b"
DOMAIN_RE = r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
URL_RE = r"https?://[^\s]+"
EMAIL_RE = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

def parse_iocs(data):
    results = set()

    for ip in re.findall(IP_RE, data):
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.is_private or ip_obj.is_loopback:
                continue
            results.add((ip, "ip"))
        except:
            pass

    for h in re.findall(HASH_RE, data):
        results.add((h.lower(), "hash"))

    for url in re.findall(URL_RE, data):
        results.add((url.lower(), "url"))

    for email in re.findall(EMAIL_RE, data):
        results.add((email.lower(), "email"))

    for d in re.findall(DOMAIN_RE, data):
        results.add((d.lower(), "domain"))

    return results
