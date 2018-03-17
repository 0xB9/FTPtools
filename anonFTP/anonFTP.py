#!/usr/bin/python
import ftplib
import time


def anonFTP(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anon@anon.com')
        print "\n[+] "+str(hostname)+" Anonymous Login Access!"
        ftp.quit()
        return True
    except Exception, e:
        print "\n[-] "+str(hostname)+" Anonymous Login Not Supported..."
        return False

print "anonFTP Login Scan"
print "Made By: 0xB9"
time.sleep(1)

host = raw_input("Enter A Host-> ")
anonFTP(host)
