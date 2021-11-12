import argparse
from core.nmap.nmap_module import Nmap
import socket

parser = argparse.ArgumentParser(description='Crack Head Hacking Tool')

def __register_arguments():
    parser.add_argument('-pS', '--port-scan', help='Port scan with target host')

def __parse_arguments():
    return parser.parse_args()
def __run():
    print("Running stuff i dont know about")


if __name__ == '__main__':
    nmap_scanner = Nmap()
    __register_arguments()
    args = __parse_arguments()

    if args.port_scan:
        ip_address = socket.gethostbyname_ex(args.port_scan)
        result = nmap_scanner.scan_ports(args.port_scan)
        print(result["scan"][str(ip_address[2].pop())])
    __run()
