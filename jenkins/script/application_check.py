#!/usr/bin/python

import socket
import sys
import ast
import argparse

check_mk_live = "/omd/sites/adm_game/tmp/run/live"
execfile("./application_check_dict.py")

def application_check(application, server):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(check_mk_live)
    if application in query_check:
        data = query_check[application].replace("tmp_srv", server)
    else:
        print("{} is not defined in check_dict".format(application))
        sys.exit(1)
    sock.sendall(data)
    services = ast.literal_eval(sock.recv(4096))
    sock.close()
    
    retval = 0
    if not services:
        retval = 10
        print "No check for %s on %s" %(application, server)
    else:
        for service in services:
            print service
            if service[2] != 0 and service[4] == 0:
                print "%s failed on %s" %(service[1], service[0])
                retval = 1

    return retval

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Application checks")
    parser.add_argument("application", help="application need to be checks")
    parser.add_argument("server", help="on server")
    args = parser.parse_args()
    retval = application_check(args.application, args.server)
    if retval == 0:
        sys.exit(0)
   
    sys.exit(retval)

