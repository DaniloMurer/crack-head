import argparse
import pandas as pd

from core.nmap.nmap_module import Nmap
from core.brute_force.brute_force_module import SSHBruteForce
from core.web.scan import WebScan
import socket

parser = argparse.ArgumentParser(description='Crack Head Hacking Tool')


def __register_arguments():
    parser.add_argument('-pS', '--port-scan', help='Port scan with target host')
    parser.add_argument('-e', '--export', help='Export result as Excel')
    parser.add_argument('-fS', '--full-scan', help='Execute full scan of target')
    parser.add_argument('-sBF', '--ssh-brute-force', help='Start SSH Brute Force attack')
    parser.add_argument('-uPwL', '--use-password-list', help='User Password list for Brute Force attacks')
    parser.add_argument('-wS', '--web-scan', help='Scan website for unwanted resources in web root')


def __parse_arguments():
    return parser.parse_args()


if __name__ == '__main__':
    nmap_scanner = Nmap()
    __register_arguments()
    args = __parse_arguments()
    current_df = None
    ssh_bruteforce = SSHBruteForce()

    if args.port_scan:
        ip_address = socket.gethostbyname_ex(args.port_scan)
        result = nmap_scanner.scan_ports(args.port_scan)
        # print(result["scan"][str(ip_address[2].pop())]['tcp'])
        filtered = result["scan"][str(ip_address[2].pop())]['tcp']
        my_dict = {}
        for item in filtered.items():
            my_dict[item[0]] = item[1]['name']
        df = pd.DataFrame(list(my_dict.items()), columns=['Port', 'Service'])
        current_df = df
        print(df)

    if args.full_scan:
        ip_address = socket.gethostbyname_ex(args.full_scan)
        result = nmap_scanner.scan_ports(args.full_scan)
        filtered = result["scan"][str(ip_address[2].pop())]['tcp']
        ports = []
        service = []
        name = []
        my_dict = {}
        for item in filtered.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.connect((args.full_scan, item[0]))
                sock.send(b'GET HTTP/1.1 \r\n')
                response = sock.recv(1024)
                name.append(str(response).strip())
            except Exception as e:
                name.append('NaN')
            ports.append(item[0])
            service.append(item[1]['name'])
        complete = list(zip(ports, service, name))
        df = pd.DataFrame(complete, columns=['Port', 'Service', 'Banner'])
        print(df)
        current_df = df

    if args.ssh_brute_force:
        if args.use_password_list:
            with open(args.use_password_list, 'r') as f:
                passwords = f.readlines()
                ssh_bruteforce.start_attack(host=args.ssh_brute_force, port=22, tries=3, passwords=passwords)
        ssh_bruteforce.start_attack(host=args.ssh_brute_force, port=22, tries=3)

    if args.web_scan:
        web_scanner = WebScan(url=args.web_scan)
        current_df = web_scanner.scan()


    if args.export:
        current_df.to_excel(args.export, index=False, sheet_name='Export')
