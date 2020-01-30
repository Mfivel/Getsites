{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #Phython 2.7 script to search s#.conf files for live sites damain name and s# user\
\
import glob\
import re\
\
count = 0\
sitesList = glob.glob('/etc/nginx/sites-enabled/s*.conf')\
regex = re.compile("    server_name* ", 50)\
\
for f in sitesList:\
    with open(f,"r") as infile:\
        while True:\
            s = infile.readline()\
            if re.match(regex, s ) is not None:\
                print f.split('ed/', 1) [1]\
                print(s)\
                count = count  + 1\
\
           # print(s)\
            if not s: break\
\
print("Total sites : ", count/2)}