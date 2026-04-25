# DNSLookup CLI — Project Overview

---

## 🌐 What This Project Does

This is a professional **DNS reconnaissance tool** built as a command-line application.

It performs:
- DNS queries  
- Reverse lookups  
- DNS resolution tracing  
- WHOIS information gathering  

The tool is designed for **network analysis, cybersecurity research, and understanding DNS infrastructure at a technical level**.

Unlike simple `dig` or `nslookup` wrappers, this project implements:
- Concurrent DNS queries  
- Full DNS resolution path tracing (Root → TLD → Authoritative)  
- Structured output for both humans and automation  

---

## ⚙️ Core Capabilities

---

### 🔍 DNS Record Queries (`cli.py`)

- Query multiple record types (A, AAAA, MX, NS, TXT, CNAME, SOA)
- Custom DNS server selection (e.g., 8.8.8.8)
- Configurable timeouts
- JSON output for automation pipelines

---

### 🔁 Reverse DNS Lookup (`cli.py`)

- IPv4 and IPv6 PTR resolution
- Identifies hostname behind IP
- Useful for:
  - Infrastructure identification
  - Hosting pattern analysis

---

### 🧵 DNS Trace (`cli.py`)

- Traces full DNS resolution path:
  **Root → TLD → Authoritative Nameserver**
- Shows delegation hierarchy
- Displays intermediate DNS servers involved

---

### 📂 Batch Operations (`cli.py`)

- Scan multiple domains from file
- Concurrent execution for performance
- Export results in JSON format

---

### 🌐 WHOIS Lookup (`cli.py`)

- Domain registration details
- Registrar information
- Creation & expiration dates
- Name server metadata

---

## 🛡️ Why This Matters for Security

DNS is a **critical attack surface** in cybersecurity.

This tool helps understand:

### 🔍 Reconnaissance Techniques
How attackers map infrastructure using DNS enumeration

### 🧠 DNS Architecture
Understanding delegation helps detect spoofing and hijacking

### 📡 Information Leakage
DNS often exposes internal systems and cloud assets

### 🚨 Attack Detection
Identify abnormal or suspicious DNS patterns

---

## 💀 Real-World Security Incidents

- **Dyn DDoS Attack (2016)**  
  Large-scale DNS disruption affecting Twitter, Netflix, Reddit

- **Sea Turtle Campaign (2019)**  
  Nation-state DNS hijacking operation  
  *(MITRE ATT&CK: T1584.002)*

- **DNSpionage (2018)**  
  DNS-based credential harvesting campaign

---

## 🏗️ Technical Architecture
User Command ->
CLI Layer (cli.py) ->
Resolver Layer (dnspython async wrapper) ->
DNS Protocol Execution ->
Output Formatter (Rich UI) ->
Terminal / JSON Output


---

### 🧩 Architecture Layers

- **CLI Layer** → Command parsing & user input  
- **Resolution Layer** → DNS protocol operations  
- **Presentation Layer** → Output formatting & display  

---

## 📚 Learning Path

This project helps you understand:

- DNS protocol mechanics (how queries work)
- Async Python for concurrent network tasks
- CLI tool design using Typer-style structure
- Error handling in network systems
- Security thinking (defender + attacker mindset)

---

## 🚀 Quick Start Examples

```bash
# Basic DNS query
dnslookup query example.com
```

```bash
# Specific record types
dnslookup query example.com --type A,MX --server 8.8.8.8
```

```bash
# DNS resolution trace
dnslookup trace example.com
```

```bash
# Reverse IP lookup
dnslookup reverse 8.8.8.8
```

```bash
# Batch scanning
echo "example.com" > domains.txt
dnslookup batch domains.txt --output results.json
```

---

## 📁 Key Files

| File | Purpose |
|------|--------|
| cli.py | Command interface |
| resolver.py | DNS logic engine |
| output.py | Terminal formatting |
| whois.py | WHOIS operations |

---

## 🔐 Security Features

- No caching → ensures fresh DNS data  
- Custom DNS server support  
- Timeout handling for reliability  
- Transparent error reporting  

---

## 🧠 What You'll Build On Top of This

After completing this project, you can extend it into:

- DNS threat intelligence systems  
- Subdomain enumeration engines  
- DNS tunnel detection tools  
- Security monitoring dashboards  

---

## 🌍 Real-World Applications

- Penetration Testing (Recon phase)  
- Incident Response investigations  
- Threat Hunting (C2 tracking)  
- Security research  
- Infrastructure auditing  

---

## ⚔️ Attack Vectors This Helps Understand

- DNS Reconnaissance (MITRE T1590.002)  
- DNS Tunneling  
- Cache Poisoning  
- Subdomain Enumeration  
- DNS-based DDoS Amplification  

---

## ➡️ Next Step

Go to `01-CONCEPTS.md` to understand DNS fundamentals and how this tool works at protocol level.
