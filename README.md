## 🔥 DNSLookup CLI — Cybersecurity Recon Tool

A powerful Python-based DNS reconnaissance tool built for **security engineers, bug bounty hunters, and learners**.

This CLI tool performs DNS enumeration, WHOIS lookups, subdomain brute forcing, and DNS tracing — all in one place.

---

# 🚀 Features

### 🔍 DNS Enumeration

* A, AAAA, MX, NS, TXT, CNAME, SOA records
* Clean terminal output using Rich

### 🔁 Reverse Lookup

* Convert IP → Domain (PTR resolution)

### 🌐 WHOIS Lookup

* Domain registration details
* Ownership & metadata

### 🧵 DNS Trace (dig +trace style)

* Root → TLD → Authoritative servers
* Nameserver IP resolution included

### 📂 Batch Scanning

* Scan multiple domains from a file
* Multithreaded execution ⚡

### 💀 Subdomain Brute Force

* Discover hidden subdomains
* Supports custom wordlists
* Fast parallel execution

### 💾 JSON Output Export

* Save results for automation
* Useful for pipelines & reporting

---

# ⚙️ Installation

```bash
git clone https://github.com/yourusername/dnslookup-cli.git
cd dnslookup-cli
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

# ▶️ Usage

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

---

# 💾 Save Output

```bash
python -m dnslookup.cli query google.com --json --output result.json
```

---

# 📄 Example Wordlist

```text
www
mail
api
admin
dev
test
blog
staging
```

---

# 🧠 Tech Stack

* Python 🐍
* dnspython
* rich (CLI UI)
* concurrent.futures (multithreading)
* socket
* whois

---

# 📁 Project Structure

```bash
dnslookup/
│── core.py        # Core logic (DNS, trace, brute)
│── cli.py         # CLI interface
│── utils.py       # Output formatting
│
├── wordlist.txt
├── requirements.txt
└── README.md
```

---

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

**Tawa Jagtap**
📧 [jagtaptanishqa03@gmail.com](mailto:jagtaptanishqa03@gmail.com)
📸 @tanishqaaaa._

---

# ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🚀 Share it

---

# 🔥 Future Improvements

* Banner grabbing
* ASN lookup
* Subdomain takeover detection
* API integrations

---

# 📜 License

MIT License
