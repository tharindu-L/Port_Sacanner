import socket

ip = (input("Enter the IP address or domain name : "))
start_port = int(input("Enter the start port : "))
end_port = int(input("Enter the end port : "))

target_ip = socket.gethostbyname(ip)


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")
        s.close()
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")


print(f"Scanning {target_ip} from port {start_port} to port {end_port}\n")

for port in range(start_port, end_port + 1):
    scan_port(target_ip, port)
