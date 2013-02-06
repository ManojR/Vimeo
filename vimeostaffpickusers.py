#!/usr/bin/python -tt

# This program is use to get the information of user's url who are having staffpick status

import MySQLdb
import sys
from urllib import urlopen
import re
import time

db = MySQLdb.connect(host='localhost',user='root',passwd='mysqlmanoj',db='vimeo')

vimeo = 'http://vimeo.com'
d ={}

with db:
  
  cur = db.cursor(MySQLdb.cursors.DictCursor)

  cur.execute("SELECT url FROM staffpick")
  numrows = int(cur.rowcount)

  for i in range(numrows):
    row = cur.fetchone()
    page = urlopen('http://'+row['url']).read()
    ph = re.search(r'"pag\w+_head\w+"',page)
    time.sleep(2)
    reget = ph.group()
    start = page.find(reget)
    hf = page.find('<a href=',start+1)
    hf1 = page.find('"',hf+1)
    hf2 = page.find('"',hf1+1)
    n = page[hf1:hf2]
    nam = n.split('"')
    name = nam[1]
    cur1 = db.cursor(MySQLdb.cursors.DictCursor)
    cur1.execute('INSERT INTO search_staffpick (Url) VALUES (%s);', (name))
    db.commit()

db.close()
