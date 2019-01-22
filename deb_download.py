#!/usr/bin/python

import argparse
import adm_deb_download
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='download package from link provided by developers')
    parser.add_argument("pkgurl", help="url to pkg")
    parser.add_argument("location", nargs='?', default=os.getcwd(), help="where to place downloaded package")
    args = parser.parse_args()
    deb = adm_deb_download.DebDownload(args.pkgurl, args.location)
    deb.download()
    
