import bs4 as bs
import requests
import random
import urllib.request
import re

def recipe(food):
  words=food.split(" ")
  new=""
  for i in words:
    new+=i+'+'
  fin='https://www.youtube.com/results?search_query='+new+'recipe'
  html = urllib.request.urlopen(fin)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  select=video_ids[0]
  link="https://www.youtube.com/watch?v="+select
  return link

def dessert():
  dessert1='https://www.delicious.com.au/recipes/collections/gallery/28-comforting-desserts-to-make-this-weekend/9l4355gd?page=3'
  sourced1= requests.get(dessert1).text
  soupd1=bs.BeautifulSoup(sourced1,'lxml')
  sweet1=[]
  eld1=soupd1.find_all("h2")
  for i in eld1:
    clean=i.find_all("a")
    sweet1.append(clean[0].contents[0])

  dessert2='https://www.taste.com.au/baking/galleries/100-instantly-comforting-desserts-nanna-used-make/onc89g9r?page=31'
  sourced2= requests.get(dessert2).text
  soupd2=bs.BeautifulSoup(sourced2,'lxml')
  eld2=soupd2.find_all("h1",{"class":"slide-title"})
  sweet2=[]
  for i in eld2:
    con=i.find_all("a")
    sweet2.append(con[0].contents[0])
  return sweet1+sweet2

def pickdessert():
  des=random.choice(dessert())
  lk=recipe(des)
  return des,lk