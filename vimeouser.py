#!/usr/bin/python -tt

# This program is to get the user's name,url,plus and upload information

import MySQLdb
import sys
from urllib import urlopen
import re

start = 5000
unum = 355000
vimeo = 'http://vimeo.com/user'
videos = '/videos'
counter = 0

db = MySQLdb.connect(host='localhost',user='root',passwd='mysqlmanoj',db='vimeo')
cursor = db.cursor()

while start >= counter:
  
  page = urlopen(vimeo+str(unum)).read()
  
  pnf = re.search(r'V\w+U\w+O\w+',page)
  chk = pnf.group()
  check = chk.startswith('VimeUhOh')

  if check == True:
    unum=unum+1
    
    if counter <= 0:
      counter = 0
    else:
      counter = counter - 1
    
  else:

    url = vimeo+str(unum)
    n = page.find('title"')
    n1 = page.find('"',n+1)
    n2 = page.find(' ',n1+1)
    n3 = page.find('co',n2+1)
    n4 = page.find('=',n3+1)
    n5 = page.find('"',n4+1)
    n6 = page.find('"',n5+1)
    user_name = page[n5+1:n6] # name


    try:
      bp = re.search(r'bad\w+_p\w+',page)
      bp_str = str(bp.group())
    except AttributeError:
      user_plus = 'N'
    else:
      user_plus = 'Y'  #plus
   
    try:
      upage = urlopen(url+videos).read()
      upld = re.search(r'0\sV\w+',upage)
      uplod = upld.group()
    except AttributeError:
      user_upload = 'Y'
    else:
      user_upload = 'N' # Upload

    counter = counter + 1
    unum=unum+1

    cursor.execute('INSERT INTO search_vimeo (url,name,plus,upload) VALUES (%s,%s,%s,%s);', (url,user_name,user_plus,user_upload))
    db.commit()

db.close()


  