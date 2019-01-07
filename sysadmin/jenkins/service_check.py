#! /usr/bin/python
import urllib
import argparse
import sys
import socket

port_dict = {"trungop": [80], "smartfox": [9933, 10843, 12888 ], "cms_backend": []}
url_dict = {"trungop": {"80": "OK"}, "smartfox": {"10880": "OK"}}

parser = argparse.ArgumentParser(description='Check services availability')
parser.add_argument("application", choices=list(port_dict.keys()), help="application to check")
parser.add_argument("server", help="on server")
args = parser.parse_args()

# Check port
def check_port():
    if port_dict.get(args.application) is None:
        print "%s doesnt have any port list" %(args.application)
        sys.exit(1)
    else:
        # Open a socket to check port
        for port in port_dict[args.application]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock_connect = sock.connect_ex((args.server, port))
            sock.close()
            if sock_connect != 0:
                print "%s is not opened on %s" %(port, args.server)
                sys.exit(1)
            else:
                print "%s is opened on %s" %(port, args.server)

# Check urls
def check_urls():
    if url_dict.get(args.application) is not None:
        for url, return_string in url_dict[args.application].iteritems():
            full_url = "http://%s:%s" %(args.server, url)
            response = urllib.urlopen(full_url)

            # Check code
            if response.getcode() >= 400:
                print "code %d retrieved" %(response.getcode())
                sys.exit(1)
            else:
                # Check return string
                if return_string != "OK":
                    print "%s doesnt contains %s" %(full_url, return_string)
                    sys.exit(1)
                else:
                    print "%s contains %s" %(full_url, return_string) 

if __name__ == "__main__":
   check_port()
   check_urls()
   sys.exit(0)
