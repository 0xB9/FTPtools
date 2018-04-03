#!/usr/bin/python
import ftplib
import time
from huepy import *

def anonFTP(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anon@anon.com')
        print good(green(str(hostname)+" Anonymous Login Access!"))
        ftp.quit()
        return True
    except Exception, e:
        print bad(red(str(hostname)+" Anonymous Login Not Supported..."))
        return False

print green("-"*60)
print lightcyan("anonFTP Login Scan")
print lightcyan("Made By: "+italic("0xB9"))
print green("-"*60)
print ""
time.sleep(1)

host = raw_input(green("Enter A Host-> "))
anonFTP(host)
