# [
# | @Gabrielctz
# [
import os
try:
    import sys
except:
    os.system("pip install sys")
try:
    import socket as sck
except:
    os.system("pip install socket")
try:
    import threading
except:
    os.system("pip install threading")
try:
    from datetime import datetime as dt
except:
    os.system("pip install datetime")

PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    587: "SMTP (Submission)",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP Proxy",
    8443: "HTTPS Alternate",
    20: "FTP Data",
    69: "TFTP",
    79: "Finger",
    111: "RPCbind",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "Microsoft-DS (SMB)",
    465: "SMTPS",
    514: "Syslog",
    546: "DHCPv6 Client",
    547: "DHCPv6 Server",
    587: "SMTP (Submission)",
    631: "IPP",
    636: "LDAPS",
    666: "Doom",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "MS SQL Server",
    1521: "Oracle Database",
    1723: "PPTP",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy",
    8443: "HTTPS Alternate",
    9100: "Printer (JetDirect)",
    9999: "Telnet (Alt)",
    10000: "Webmin",
    27017: "MongoDB",
    27018: "MongoDB",
    27019: "MongoDB",
    28017: "MongoDB HTTP",
    49152: "UPnP",
    49153: "UPnP",
    49154: "UPnP",
    49155: "UPnP",
    49156: "UPnP",
    49157: "UPnP",
    49158: "UPnP",
    49159: "UPnP",
    49160: "UPnP",
    49161: "UPnP",
    49162: "UPnP",
    49163: "UPnP",
    49164: "UPnP",
    49165: "UPnP",
    49166: "UPnP",
    49167: "UPnP",
    49168: "UPnP",
    49169: "UPnP",
}

def version(response):
    try:
        res = response.decode('utf-8').split('\r\n')
        for line in res:
            if 'Server:' in line:
                infos = line.split('Server:')[1].strip()
                return infos
        return "Server version was not detected."
    except Exception as e:
        return print(str(e))

def scanner(target, port):
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    sck.setdefaulttimeout(0.5)
    results = s.connect_ex((target, port))
    service = PORT_SERVICES.get(port, "Service inconnu/privé.")
    protocol = "TCP" 
    if results == 0:
        print(f"Port {port} | {service} | {target} ({protocol})")
        if port == 80:
            try:
                s.send(b'GET / HTTP/8.3\r\nHost: amazon.com\r\n\r\n')
                response = s.recv(1024)
                infos = version(response)
                print(f"Host version: {infos}")
            except:
                pass

if len(sys.argv) == 2:
    target = sck.gethostbyname(sys.argv[1])
else:
    print("Syntax: python3 script.py [ip/hostname]")
    sys.exit(1)

print(f"Scanning target: {target}")
print("Time started: " + str(dt.now()))
print('-' * 50)

try:
    threads = []
    for port in range(1, 65536):
        thread = threading.Thread(target=scanner, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

except:
    pass
