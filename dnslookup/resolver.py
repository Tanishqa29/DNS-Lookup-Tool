import dns.resolver
from dnslookup.models import DNSRecord, DNSResult

def lookup(domain: str):
    records = []
    errors = []

    try:
        answers = dns.resolver.resolve(domain, "A")
        for r in answers:
            records.append(DNSRecord(type="A", value=r.to_text(), ttl=answers.rrset.ttl))
    except Exception as e:
        errors.append(str(e))

    return DNSResult(domain=domain, records=records, errors=errors)