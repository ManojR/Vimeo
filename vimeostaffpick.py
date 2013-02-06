#!/usr/bin/python -tt

# This program is used to get the information of staffpick videos urls

import MySQLdb
import sys
import urllib
from urllib import urlretrieve
from urllib import urlopen
import re
import os

db = MySQLdb.connect(host='localhost',user='root',passwd='mysqlmanoj',db='vimeo')
cursor = db.cursor()

v = 'www.vimeo.com'
vst = "http://vimeo.com"
vmst = "/channels/staffpicks/videos/page:"
vest = "/sort:preset"


nt=1
r=2

upt = []

for nt in range(1,513):

  jj = str(nt)
  htt = vst+vmst+jj+vest

  page =  urlopen(htt).read()

  s = re.findall(r'<a\sh\w+="/c\w+/s\w+/\w+"',page)
  vs = 'www.vimeo.com/'
  for i in range(len(s)-2):
   sp = str(s[i]).split('/')
   sp1 = sp[3]
   getsp = sp1.split('"')
   upt.append(vs+str(getsp[0]))

for r in range(len(upt)):
  cursor.execute('INSERT INTO staffpick (url) VALUES (%s);', (upt[r]))
  db.commit()
  
db.close()
