# 🧿 DNSRecordInjector

A lightweight Python script for dynamically updating DNS A records on servers that allow unsigned updates (RFC 2136). Perfect for testing, red teaming, or automating DNS record changes in lab environments.

## 🚀 Features

- Dynamically adds A records to a specified DNS zone.
- Interactive prompts for user-friendly input.
- Validates IP addresses to ensure correctness.
- Supports unsigned updates (no TSIG authentication).
- Uses `dnspython` and Python standard libraries.

## 🛠️ Requirements

- Python 3.8+
- `dnspython` library

Install the required library with:

```bash
pip install dnspython
```

## 📦 Usage

Run the script with:

```bash
python3 dns_update.py
```

Follow the interactive prompts:

```text
🔧 DNS A Record Adder (Dynamic Update)

🖥️  Enter DNS server IP: 192.168.1.53
🌐 Enter domain (zone) [e.g., example.com.]: lab.local
📛 Enter record name (e.g., www): test1
📍 Enter IP address for the A record: 192.168.1.100

📤 Sending DNS update request...
✅ DNS update response:
...
```

## 🔐 Notes

- This script assumes the DNS server allows unauthenticated updates, often found in misconfigured internal networks or lab setups.
- Ideal for testing, internal infrastructure automation, or exploitation during authorized security assessments.

## ⚠️ Disclaimer

This tool is for educational and authorized testing purposes only. Do not use it on networks or systems without explicit permission.

## 📂 License

MIT License
