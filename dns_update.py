import dns.update
import dns.query
import dns.exception
import dns.resolver
import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def main():
    print("🔧 DNS A Record Adder (Dynamic Update)\n")

    # 🖥️ Ask the user for the target DNS server IP
    while True:
        dns_server = input("🖥️  Enter DNS server IP: ").strip()
        if is_valid_ip(dns_server):
            break
        print("❌ Invalid IP address. Try again.")

    # 🌐 Get the zone name (must end with a dot)
    domain = input("🌐 Enter domain (zone) [e.g., example.com.]: ").strip()
    if not domain.endswith('.'):
        domain += '.'

    # 📛 Name of the record to create within the zone
    record = input("📛 Enter record name (e.g., www): ").strip()

    # 📍 Destination IP for the A record
    while True:
        ip = input("📍 Enter IP address for the A record: ").strip()
        if is_valid_ip(ip):
            break
        print("❌ Invalid IP address. Try again.")

    # 🧱 Craft the update payload (unsigned, no TSIG used)
    update = dns.update.Update(domain)
    update.add(record, 300, 'A', ip)

    # 🚀 Push the update to the DNS server over TCP
    try:
        print("\n📤 Sending DNS update request...")
        response = dns.query.tcp(update, dns_server, timeout=5)
        print("✅ DNS update response:")
        print(response)
    except dns.exception.DNSException as e:
        print(f"❌ DNS update failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
