#! /usr/bin/python

import adm_deploy
import adm_pkginfo
import argparse

class ADMDeploy:
    def __init__(self, _srv, _pkg):
        self.pkg = _pkg
        self.srv = _srv
  
    def deploy(self):
        d = adm_deploy.JDeploy(self.pkg, self.srv)
        d.dry_deploy()
        d.deploy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='deploy packages to server/group')
    parser.add_argument("-p", "--package", help="packages to be installed")
    parser.add_argument("-m", "--machine", help="which server")
    args = parser.parse_args()

    admdeploy = ADMDeploy(args.machine, args.package)
    print "Deploying ..."
    admdeploy.deploy()
