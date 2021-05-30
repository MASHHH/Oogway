import requests 
from bs4 import BeautifulSoup 
import random

def motivate():
  url1='https://www.allquotesabout.com/motivational-quotes/'
  source1= requests.get(url1).text
  soup1=BeautifulSoup(source1,'lxml')
  elq1=soup1.find_all("div",{"class":"wp-block-image"})
  links1=[]
  for i in elq1:
    img=i.find_all("img")[0]['data-large-file']
    links1.append(img)

  url2="https://everydaypower.com/inspirational-quotes-with-pictures/"
  source2= requests.get(url2).text
  soup2=BeautifulSoup(source2,'lxml')
  elq2=soup2.find_all("div",{"class":"wp-block-image"})
  links2=[]
  for i in elq2:
    img=i.find_all("img")[0]['src']
    links2.append(img)
  
  return random.choice(links1+links2)

