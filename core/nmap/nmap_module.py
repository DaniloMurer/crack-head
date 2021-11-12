import nmap
import json

class Nmap:

    def __init__(self):
        self.port_scanner = nmap.PortScanner()

    def scan_ports(self, host: str):
        return self.port_scanner.scan(host, arguments='-Pn')

