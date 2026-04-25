import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from rich import print as rprint

from dnslookup.core import (
    get_dns_records,
    reverse_lookup,
    whois_lookup,
    trace_dns,
    brute_subdomains
)
from dnslookup.utils import print_dns, print_message, print_trace


def process_domain(domain):
    print_message("\n" + "=" * 50)
    print_message(f"Checking: {domain}")
    records = get_dns_records(domain)
    print_dns(records)


def main():
    parser = argparse.ArgumentParser(description="DNSLookup CLI Tool")

    parser.add_argument("command", help="query | reverse | whois | batch | trace | brute")
    parser.add_argument("target", help="domain / ip / file")
    parser.add_argument("--json", action="store_true", help="Output in JSON")
    parser.add_argument("--output", help="Save output to file (json)")

    args = parser.parse_args()

    # 🔍 QUERY
    if args.command == "query":
        records = get_dns_records(args.target)

        if args.json:
            print_message("JSON Output:\n")
            rprint(records)

            if args.output:
                with open(args.output, "w") as f:
                    json.dump(records, f, indent=4)
                print_message(f"Saved to {args.output}")
        else:
            print_dns(records)

    # 🔁 REVERSE
    elif args.command == "reverse":
        result = reverse_lookup(args.target)
        print_message(f"Reverse Lookup: {result}")

    # 🌐 WHOIS
    elif args.command == "whois":
        result = whois_lookup(args.target)
        print_message(str(result))

    # 🔥 TRACE
    elif args.command == "trace":
        steps = trace_dns(args.target)
        print_trace(steps)

        if args.output:
            with open(args.output, "w") as f:
                json.dump(steps, f, indent=4)
            print_message(f"Saved to {args.output}")

    # 📂 BATCH
    elif args.command == "batch":
        try:
            with open(args.target, "r") as f:
                domains = [d.strip() for d in f if d.strip()]

            with ThreadPoolExecutor(max_workers=5) as executor:
                executor.map(process_domain, domains)

        except FileNotFoundError:
            print_message("File not found!")

    # 💀 SUBDOMAIN BRUTE
    elif args.command == "brute":
        try:
            with open(args.target, "r") as f:
                wordlist = [w.strip() for w in f if w.strip()]

            domain = input("Enter target domain: ")

            print_message("\nStarting subdomain brute force...\n")

            found = brute_subdomains(domain, wordlist)

            if found:
                for sub, ips in found:
                    print_message(f"{sub} → {', '.join(ips)}")
            else:
                print_message("No subdomains found")

        except FileNotFoundError:
            print_message("Wordlist file not found!")

    else:
        print_message("Invalid command")


if __name__ == "__main__":
    main()
