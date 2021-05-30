import urllib.request
import re
import random

def ytlink(query):
  words=query.split(" ")
  new=""
  for i in words:
    new+=i+'+'
  fin='https://www.youtube.com/results?search_query='+new
  html = urllib.request.urlopen(fin)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  select=random.choice(video_ids[:10])
  link="https://www.youtube.com/watch?v="+select
  return link

def song(singer):
  lk= ytlink(singer+" songs")
  return lk

def animal(pet):
  lk= ytlink('cute '+pet+" videos")
  return lk

