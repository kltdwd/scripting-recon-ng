#!/usr/bin/python
# -*- coding: utf-8 -*-

# Subdomain enumeration script that creates a dynamic resource script for recon-ng.
# inspired by @jhaddix bash script

from sys import argv
from datetime import date
import subprocess
import os

wordlist = "/usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1mil-5000.txt"

pwd = os.getcwd()
dir = os.path.join(pwd, '')

# input from command-line becomes domain to test
domain = argv[1]
today = date.today()
filename = domain + "-" + str(today) + ".resource"

modules = {
    "recon/domains-hosts/google_site_web",
    "recon/domains-hosts/bing_domain_web",
    "recon/domains-hosts/netcraft",
    "recon/hosts-hosts/resolve"
}

#create rc file with workspace.timestamp and start enumerating hosts
target = open (filename, 'w') ## a will append, w will over-write

workspaceline = "workspaces select " + domain + "-" + str(today) + '\n'
target.write(workspaceline)

for m in modules:
    target.write("use " + m + '\n')
    target.write("set SOURCE " + domain + '\n')
    target.write("run" + '\n')

print "Modules added to RC file"

target.write("use recon/domains-hosts/brute_hosts" + '\n')
target.write("set SOURCE " + domain + '\n')
target.write("set WORDLIST " + wordlist + '\n')
target.write("run" + '\n')

target.write("use recon/hosts-hosts/resolve" + '\n')
target.write("run" + '\n')

target.write("use reporting/csv" + '\n')
target.write("set FILENAME " + dir + domain + ".csv" + '\n')
target.write("run" + '\n')

target.close()

respath = os.path.join(pwd, str(filename))
reconcmd = '/usr/bin/recon-ng --no-check -r '.split()
subprocess.call('/usr/bin/recon-ng --no-check -r ' + respath, shell=True)
