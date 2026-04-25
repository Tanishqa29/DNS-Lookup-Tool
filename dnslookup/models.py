from dataclasses import dataclass
from typing import Optional, List

@dataclass
class DNSRecord:
    type: str
    value: str
    ttl: Optional[int] = None
    priority: Optional[int] = None


@dataclass
class DNSResult:
    domain: str
    records: List[DNSRecord]
    errors: List[str]