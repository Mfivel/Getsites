#Python 2.7 script to search s#.conf files for live sites domain name and s# user

import glob
import re

count = 0
sitesList = glob.glob('/etc/nginx/sites-enabled/s*.conf')
regex = re.compile("    server_name* ", 50)

for f in sitesList:
    with open(f,"r") as infile:
        while True:
            s = infile.readline()
            if re.match(regex, s ) is not None:
                print f.split('ed/', 1) [1]
                print(s)
                count = count  + 1

           # print(s)
            if not s: break

#print("Total sites : ", count/2)
