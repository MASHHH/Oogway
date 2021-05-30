import requests
import bs4 as bs
import random

def hollywood():
  moviehw="https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/"
  rtlink="https://www.rottentomatoes.com/"
  sourcehw= requests.get(moviehw).text
  souphw=bs.BeautifulSoup(sourcehw,'lxml')
  elhw=souphw.find_all("tr")
  td=[]
  for i in elhw:
    l=i.find_all("td")
    if len(l)==4:
      td.append(l)
  hw_names=[]
  hw_desc=[]
  for j in td:
    a=j[2].contents
    b=a[1].contents
    c=a[1]['href']
    hw_names.append(b[0].lstrip("\n "))
    hw_desc.append(rtlink+c)
  
  n=random.randint(0,99)
  return hw_names[n], hw_desc[n]

def bollywood():
  moviebw="https://www.imdb.com/list/ls004221468/"
  head="https://www.imdb.com"
  tail="?ref_=ttls_li_tt"
  sourcebw= requests.get(moviebw).text
  soupbw=bs.BeautifulSoup(sourcebw,'lxml')
  elbw=soupbw.find_all("h3")
  bw_names=[]
  bw_desc=[]
  for i in elbw[:100]:
    a=i.find_all("a")
    bw_names.append(a[0].contents[0])
    bw_desc.append(head+a[0]['href']+tail)
  
  n=random.randint(0,99)
  return bw_names[n], bw_desc[n]