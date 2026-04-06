# DNS Lookup Tool — Project Overview

## 🚀 What This Project Does

This is a professional DNS reconnaissance tool built as a command-line application. It performs DNS queries, reverse lookups, resolution tracing, and WHOIS information gathering.

The tool is designed for:
- Network analysis
- Security research
- Understanding DNS infrastructure at a technical level

Unlike simple `dig` or `nslookup` wrappers, this project implements:
- Concurrent async DNS queries ⚡
- Resolution path tracing from root servers
- Structured output for both humans and automation (JSON)

---

## ⚙️ Core Capabilities

### 🔍 DNS Record Queries
*(dnslookup/cli.py:112–167)*

- Query multiple record types simultaneously:
  - A, AAAA, MX, NS, TXT, CNAME, SOA
- Custom DNS server selection
- Configurable timeouts
- JSON output support for parsing

---

### 🔁 Reverse DNS Lookups
*(dnslookup/cli.py:170–216)*

- IPv4 and IPv6 PTR resolution
- Useful for:
  - Identifying server ownership
  - Detecting hosting patterns

---

### 🧵 DNS Trace
*(dnslookup/cli.py:219–263)*

- Traces full resolution path:
  - Root → TLD → Authoritative
- Visualizes DNS delegation hierarchy
- Shows which servers are queried at each step

---

### 📂 Batch Operations
*(dnslookup/cli.py:266–350)*

- Process multiple domains from a file
- Concurrent async execution for speed ⚡
- Export results to JSON

---

### 🌐 WHOIS Lookups
*(dnslookup/cli.py:353–393)*

- Domain registration details
- Registrar information
- Creation & expiration dates
- Nameserver data

---

## 🛡️ Why This Matters for Security

DNS is a **critical attack surface** in cybersecurity.

This project helps you understand:

- **Reconnaissance Techniques**  
  → How attackers map infrastructure  

- **DNS Architecture**  
  → Delegation & resolution flow  

- **Information Leakage**  
  → What DNS exposes publicly  

- **Attack Detection**  
  → Identifying suspicious patterns  

---

### ⚠️ Real-World Incidents

- **Dyn DDoS Attack (2016)**  
  → Took down Twitter, Netflix, Reddit  

- **Sea Turtle Campaign (2019)**  
  → Nation-state DNS hijacking  
  → MITRE ATT&CK: T1584.002  

- **DNSpionage (2018)**  
  → Credential harvesting via DNS hijack  

---

## 🏗️ Technical Architecture
