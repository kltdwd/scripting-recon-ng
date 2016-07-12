Subdomain enumeration script that creates a resource file for recon-ng and then runs the relevant modules (google, netcraft, bing and bruteforce).
inspired by @jhaddix bash script. Written in Python, just because I wanted to.

Assumptions are;

recon-ng is installed at '/usr/bin/recon-ng'

downloaded wordlist of potential subdomains for bruteforcing - wordlist variable, line 12.

Usage:
```
python enumall.py google.com
```
This does not exit the recon-ng session. Exit the session and view the newly created csv file.
