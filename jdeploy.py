#! /usr/bin/python

import adm_deploy
import adm_pkginfo
import argparse

class ADMDeploy:
    def __init__(self, _srv):
        self.pkg_input = []	# List of input that need downloading
        self.pkgs = {}		# "pkgName": "pkgVer"
        self.srv = _srv
  
    def set_pkgs(self, pkg_list):
        for pkg_path in pkg_list:
            print pkg_path
            # Set pkg list for installing
            pkginfo = adm_pkginfo.PkgInfo(pkg_path)
            if "=" in pkg_path:
                 pkginfo.process()
                 self.pkgs[pkginfo.pkgname] = pkginfo.pkgver
            else:
                 pkginfo.no_process()
                 self.pkgs[pkginfo.pkgname] = ""

    def deploy(self):
        d = adm_deploy.JDeploy(self.pkgs, self.srv)
        d.dry_deploy()
        d.deploy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='deploy packages to server/group')
    parser.add_argument("-p", "--packages", nargs="+", help="packages to be installed")
    parser.add_argument("-m", "--machine", help="which server")
    args = parser.parse_args()

    adm_deploy = ADMDeploy(args.machine)
    adm_deploy.set_pkgs(args.packages)
    print "Deploy:"
    adm_deploy.deploy()
