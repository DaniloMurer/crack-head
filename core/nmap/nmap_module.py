import nmap
import json

class Nmap:

    def __init__(self):
        self.port_scanner = nmap.PortScanner()

    def scan_ports(self, host: str):
        #json_object = json.dumps(self.port_scanner.scan(host, arguments='-Pn'))
        #return json_object
        return self.port_scanner.scan(host, arguments='-Pn')

