# 💻 Implementation Details

---

## 🔧 Core DNS Resolution Implementation

### 📡 Single Record Type Query
async def query_record_type(domain, record_type, resolver):
- Queries one DNS record type (A, MX, TXT, etc.)
- Returns structured DNSRecord objects

### ⚙️ Key Design Decisions

- **Exception as control flow**
  - NXDOMAIN / NoAnswer → return empty list (not crash)

- **TTL handling**
  - Taken from `rrset.ttl`

- **Separation of logic**
  - Value extraction handled separately for clean design

---

## ⚡ Multi-Type Concurrent Query
async def lookup(domain, record_types):

### 🚀 How it works

- Creates async tasks for all record types
- Executes using `asyncio.gather()`

### 🔥 Why return_exceptions=True?

- Prevents full failure if one query fails
- Enables partial results

### ⏱ Performance

- Sequential: ~350ms  
- Concurrent: ~50ms ⚡

---

## 🔁 Reverse DNS Lookup
async def reverse_lookup(ip_address):

### 🧠 What it does

- Converts IP → domain (PTR record)
- Uses `.in-addr.arpa` or `.ip6.arpa`

### ⚠️ Error Handling

- NXDOMAIN → no PTR record
- Timeout → network issue
- NoNameservers → DNS failure

---

## 🌐 DNS Trace Implementation

### 🧭 Concept

Follows DNS path:
Root → TLD → Authoritative

---

### 🔥 Root Servers

- Hardcoded root servers used as bootstrap
- Example:
  - a.root-servers.net → 198.41.0.4

---

### 🔁 Main Flow

1. Query root server  
2. Get referral to TLD  
3. Query TLD server  
4. Get authoritative NS  
5. Repeat until answer found  

---

### 🧩 Glue Records

- Resolve NS → IP mapping issue
- Prevent circular dependency problem

---

## 🧾 CLI Implementation

### 🧩 Argument Parsing

- Supports:
  - `A,MX,TXT`
  - `ALL`
- Invalid types → warnings (not crash)

---

### ⏳ Progress UI

- Spinner shown during execution
- Auto disappears after completion

---

### 📂 Batch Processing

- Reads domain list from file
- Ignores:
  - empty lines
  - comments (#)

---

## 🎨 Output Formatting (Rich UI)

### 📊 DNS Table

- Clean tabular output
- Colored record types
- TTL formatting
- Priority display for MX

---

### 🌳 Trace Tree View
Root → TLD → Authoritative → Final Answer


- Hierarchical visualization
- Shows full DNS path

---

## 📦 JSON Output

### Supports:

- Single domain → object
- Batch scan → array

### Structure:

{
"domain": "...",
"records": [...],
"errors": [],
"query_time_ms": 12.5
}


---

## 🔐 Security Features

- ❌ No caching → always fresh data  
- 🌐 Custom DNS server support  
- ⏱ Timeout handling for stability  
- 🧾 Transparent error reporting  

---

## ⚡ Performance Design

### Async Model

- Uses `asyncio`
- Parallel DNS queries

### Speed Impact

- 7 record types → 7x faster than sequential

---

## ⚠️ Design Patterns Used

- Exceptions → results conversion  
- Defensive attribute access  
- Type-safe handling (`isinstance`)  
- Separation of logic vs UI  

---

## 🚀 Next Step

Go to **04-CHALLENGES.md** to extend this system into advanced recon and security tooling.
