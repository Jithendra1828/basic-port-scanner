import socket
from datetime import datetime

def scan_port(target_ip, port):
    """
    🔍 Scans a single port on the target IP
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"🟢 Port {port} is OPEN")
        else:
            print(f"🔴 Port {port} is closed")

        sock.close()

    except KeyboardInterrupt:
        print("\n❌ Scan interrupted by user")
        exit()

    except socket.gaierror:
        print("❌ Hostname could not be resolved")
        exit()

    except socket.error:
        print("❌ Couldn't connect to server")
        exit()


def main():
    print("=" * 50)
    print("📡 BASIC PORT SCANNER")
    print("=" * 50)

    target = input("🌐 Enter target IP or domain: ")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid hostname")
        return

    print(f"\n🎯 Scanning Target: {target_ip}")
    print("⏳ Scanning first 1000 ports...\n")

    start_time = datetime.now()

    for port in range(1, 1001):  # Scan ports 1–100
        scan_port(target_ip, port)

    end_time = datetime.now()
    duration = end_time - start_time

    print("\n" + "=" * 50)
    print("✅ Scan Completed Successfully!")
    print(f"⏱️ Time Taken: {duration}")
    print("=" * 50)


if __name__ == "__main__":
    main()
