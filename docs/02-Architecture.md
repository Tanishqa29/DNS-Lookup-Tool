# System Architecture — DNS Lookup Tool

## 🏗️ High-Level Architecture

This project follows a **modular architecture**, separating concerns into different layers for scalability, readability, and maintainability.

### Flow:
User Command (CLI)
↓
cli.py (Argument Parsing & Routing)
↓
core.py (DNS Logic & Processing)
↓
External Libraries (dnspython, socket, whois)
↓
utils.py (Formatting & Output)
↓
Terminal Display (Rich UI)

---

## 🧩 Architecture Breakdown

### 1️⃣ CLI Layer — `cli.py`

Handles:
- User input (commands like `query`, `trace`, `brute`)
- Argument parsing using `argparse`
- Routing commands to appropriate functions

Example:
```python
if args.command == "query":
    records = get_dns_records(args.target)

👉 This layer acts as the entry point of the application.

2️⃣ Core Logic Layer — core.py

This is the brain of the application.

Handles:

DNS queries (get_dns_records)
Reverse lookup (reverse_lookup)
WHOIS lookup (whois_lookup)
DNS tracing (trace_dns)
Subdomain brute force (brute_subdomains)

Example:
  answers = dns.resolver.resolve(domain, "A")

👉 Responsible for all network-level operations.

3️⃣ External Libraries Layer

Used for real-world functionality:

dnspython → DNS queries
socket → reverse lookup
whois → domain info

👉 These libraries interact with actual DNS infrastructure.

4️⃣ Presentation Layer — utils.py

Handles:

Output formatting
Rich tables & clean CLI display

Example:
    console.print(table)

👉 Converts raw data → human-readable output

🔁 Data Flow Explained

When user runs:
  python -m dnslookup.cli query google.com

Flow:

1.CLI receives command
2.CLI calls get_dns_records()
3.Core performs DNS query
4.Data returned to CLI
5.utils.py formats output
6.Result shown in terminal
