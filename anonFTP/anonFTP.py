#!/usr/bin/python
import ftplib
import time

class color:
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'

def anonFTP(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anon@anon.com')
        print color.green+"\n[+] "+str(hostname)+" Anonymous Login Access!"+color.end
        ftp.quit()
        return True
    except Exception, e:
        print color.red+"\n[-] "+str(hostname)+" Anonymous Login Not Supported..."+color.end
        return False

print color.blue+"anonFTP Login Scan"+color.end
print color.blue+"Made By: 0xB9"+color.end
time.sleep(1)

host = raw_input("Enter A Host-> ")
anonFTP(host)
