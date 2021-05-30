import random

def getsinger(id):
  import sqlite3
  mycon = sqlite3.connect('survey.db')
  cur = mycon.cursor()
  s="select singer from log where id = '{}'".format(str(id))
  cur.execute(s)
  l= cur.fetchone()[0].split(", ")
  return random.choice(l)

def getanimal(id):
  import sqlite3
  mycon = sqlite3.connect('survey.db')
  cur = mycon.cursor()
  s="select animal from log where id = '{}'".format(str(id))
  cur.execute(s)
  l= cur.fetchone()[0].split(", ")
  return random.choice(l)

def getvnv(id):
  import sqlite3
  mycon = sqlite3.connect('survey.db')
  cur = mycon.cursor()
  s="select veg_nv from log where id='{}'".format(str(id))
  cur.execute(s)
  return cur.fetchone()[0]

def getmov(id):
  import sqlite3
  mycon = sqlite3.connect('survey.db')
  cur = mycon.cursor()
  s="select hw_bw from log where id='{}'".format(str(id))
  cur.execute(s)
  return cur.fetchone()[0]
