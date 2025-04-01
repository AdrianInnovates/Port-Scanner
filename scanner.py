import socket

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[+] Port {port} is open.")
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP address: ")
    print(f"Scanning target: {target}")
    for port in range(1, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    main()
