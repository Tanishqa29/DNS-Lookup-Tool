import dns.resolver
import socket
import whois


def get_dns_records(domain):
    records = {}
    types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']

    for t in types:
        try:
            answers = dns.resolver.resolve(domain, t)
            records[t] = [str(r) for r in answers]
        except dns.resolver.NoAnswer:
            records[t] = []
        except dns.resolver.NXDOMAIN:
            records[t] = ["Domain does not exist"]
        except Exception as e:
            records[t] = [f"Error: {e}"]

    return records


def reverse_lookup(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return "Reverse lookup failed"


def whois_lookup(domain):
    try:
        return whois.whois(domain)
    except Exception:
        return "WHOIS lookup failed"


# 🔥 Resolve NS IP
def resolve_ns_ip(ns):
    try:
        answers = dns.resolver.resolve(ns, "A")
        return [str(r) for r in answers]
    except Exception:
        return ["IP not found"]


# 🔥 DNS Trace
def trace_dns(domain):

    steps = []

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8"]

        # Root
        root_ns = resolver.resolve(".", "NS")
        root_data = []
        for ns in root_ns:
            ns_name = str(ns)
            ips = resolve_ns_ip(ns_name)
            root_data.append(f"{ns_name} → {', '.join(ips)}")
        steps.append(("Root Servers", root_data))

        # TLD
        tld = domain.split(".")[-1]
        tld_ns = resolver.resolve(tld, "NS")
        tld_data = []
        for ns in tld_ns:
            ns_name = str(ns)
            ips = resolve_ns_ip(ns_name)
            tld_data.append(f"{ns_name} → {', '.join(ips)}")
        steps.append((f"TLD ({tld})", tld_data))

        # Authoritative
        auth_ns = resolver.resolve(domain, "NS")
        auth_data = []
        for ns in auth_ns:
            ns_name = str(ns)
            ips = resolve_ns_ip(ns_name)
            auth_data.append(f"{ns_name} → {', '.join(ips)}")
        steps.append((f"Authoritative ({domain})", auth_data))

        # Final A
        a_record = resolver.resolve(domain, "A")
        steps.append(("Final A Record", [str(r) for r in a_record]))

    except Exception as e:
        steps.append(("Error", [str(e)]))

    return steps


# 💀 SUBDOMAIN BRUTE FORCE (ADD HERE — LAST)
from concurrent.futures import ThreadPoolExecutor

def check_subdomain(sub, domain):
    subdomain = f"{sub}.{domain}"
    try:
        answers = dns.resolver.resolve(subdomain, "A")
        ips = [str(r) for r in answers]
        return (subdomain, ips)
    except:
        return None


def brute_subdomains(domain, wordlist):
    found = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda sub: check_subdomain(sub, domain), wordlist)

        for res in results:
            if res:
                found.append(res)

    return found
