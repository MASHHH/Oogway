import urllib.request as url
import bs4 as bs
import requests
import random
import re

def recipe(food):
  words=food.split(" ")
  new=""
  for i in words:
    new+=i+'+'
  fin='https://www.youtube.com/results?search_query='+new+'recipe'
  html = url.urlopen(fin)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  select=video_ids[0]
  link="https://www.youtube.com/watch?v="+select
  return link

food1='https://www.jetsetter.com/magazine/20-best-comfort-foods-in-the-us/'
sourcef1= url.urlopen(food1).read()
soupf1=bs.BeautifulSoup(sourcef1,'lxml')
comfort=[]
elf1=soupf1.find_all("h2",{"class":"heading"})
for i in elf1:
  a=i.contents[0].rstrip('\n\t')
  b=a.lstrip('\n\t')
  comfort.append(b)

veg='https://www.thespruceeats.com/vegetarian-comfort-food-recipes-5086173'
sourcev1= requests.get(veg).text
soupv1=bs.BeautifulSoup(sourcev1,'lxml')
elv1=soupv1.find_all("h2")
linkv1=[]
vegfood=[]
for i in elv1:
  tag=i.find_all("a")
  linkv1.append(tag[0]['href'])
  vegfood.append(tag[0].contents[0])

veg2="https://thestrongtraveller.com/2020/07/20/12-indian-comfort-foods-that-can-easily-destress-you-after-a-busy-day/"
sourcev2= requests.get(veg2).text
soupv2=bs.BeautifulSoup(sourcev2,'lxml')
elv2=soupv2.find_all("h2")
indian=[]
for i in elv2[:12]:
  b=i.find_all("b")
  name=b[0].contents[0]
  indian.append(name[3:])

def picknvfood():
  food=random.choice(comfort+indian+vegfood)
  if food in vegfood:
    n=vegfood.index(food)
    lk=linkv1[n]
  else:
    lk=recipe(food)
  return food,lk

def pickvegfood():
  food=random.choice(indian+vegfood)
  if food in vegfood:
    n=vegfood.index(food)
    lk=linkv1[n]
  else:
    lk=recipe(food)
  return food,lk