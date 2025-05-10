import socket
import threading

ip = (input("Enter the IP address or domain name : "))
start_port = int(input("Enter the start port : "))
end_port = int(input("Enter the end port : "))

target_ip = socket.gethostbyname(ip)

common_ports = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy",
}

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            print(f"[+] Port {port} is open - {service}\n")
        else:
            print(f"[-] Port {port} is closed\n")
        s.close()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def threaf_scan(ip, port):
    scan_port(ip, port)

threads = []
print(f"Scanning {target_ip} from port {start_port} to port {end_port}\n")

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=threaf_scan, args=(target_ip, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()