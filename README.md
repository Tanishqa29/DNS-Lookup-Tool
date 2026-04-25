# 🌐 DNSLookup CLI

Cybersecurity Projects | Python | Recon Tool

---

## 🔥 Overview

DNSLookup CLI is a lightweight **DNS reconnaissance tool** used for domain intelligence gathering, DNS analysis, and basic security research.

It helps security learners understand how DNS works in real-world scenarios.

---

## ⚙️ What It Does

- DNS record lookup (A, AAAA, MX, NS, TXT, CNAME, SOA)
- Reverse IP lookup
- WHOIS domain information
- DNS resolution tracing
- Batch domain scanning
- JSON export support

---

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/dnslookup-cli.git
cd dnslookup-cli
pip install -r requirements.txt
```
---

## ▶️ Usage

## 🔍 Query DNS Records

```bash
python -m dnslookup.cli query google.com
```

## 🔁 Reverse Lookup

```bash
python -m dnslookup.cli reverse 8.8.8.8
```

## 🌐 WHOIS

```bash
python -m dnslookup.cli whois google.com
```

## 🔥 DNS Trace

```bash
python -m dnslookup.cli trace google.com
```

## 📂 Batch Scan

```bash
python -m dnslookup.cli batch domains.txt
```

## 💀 Subdomain Brute Force

```bash
python -m dnslookup.cli brute wordlist.txt
```

## 💾 Save Output

```bash
python -m dnslookup.cli query google.com --json --output result.json
```

---

# 📁 Project Structure

```bash
dnslookup/
│── core.py
│── cli.py
│── utils.py
│── wordlist.txt
│── requirements.txt
│
├── docs/
│   ├── 00-overview.md
│   ├── 01-concepts.md
│   ├── 02-architecture.md
│   ├── 03-implementation.md
│   ├── 04-challenges.md
```

---

# 🧠 Learn

This project includes structured learning modules covering security theory, architecture, and implementation.

| Module | Topic |
|------|--------|
| 00 | Overview |
| 01 | Concepts |
| 02 | Architecture |
| 03 | Implementation |
| 04 | Challenge |

# 💀 Real-World Use Cases

* Bug bounty reconnaissance
* Attack surface discovery
* Domain intelligence gathering
* Security research & automation

---

# ⚠️ Disclaimer

This tool is for **educational and ethical use only**.
Do not use it on systems without proper authorization.

---

# 👩‍💻 Author

**Tanishqa Jagtap**
📧 [jagtaptanishqa03@gmail.com](mailto:jagtaptanishqa03@gmail.com)

---

