#!/usr/bin/python

import argparse
import adm_aptly
import sys

## Main
if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='upload/delete package to/from repo')
  parser.add_argument("package", help="pkg to upload")
  parser.add_argument("-u", "--url", nargs="?", default="http://repo.cardgame.cf/api", help="mirror url")
  parser.add_argument("-p", "--prod", action='store_false', help="no section modification")
  parser.add_argument("-d", "--delete", action='store_true', help="delete")
  parser.add_argument("-r", "--repo", nargs="?", help="custom repo")
  args = parser.parse_args()

  apt = adm_aptly.AptlyUpload(args.package, args.prod, args.url)
  apt.identify_repo(args.repo)
  if args.delete == True:
    apt.delete_pkg()
    apt.publish_repo()
    sys.exit(0)
  apt.pkg.print_info()
  apt.upload_file_to_repo("jenkins")
  apt.add_pkg_to_repo("jenkins")
  apt.publish_repo()

