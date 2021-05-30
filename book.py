import requests
import bs4 as bs
import random

def kitaab():
  book="https://www.buzzfeed.com/cieravelarde/harry-potter-is-truly-magical"
  sourceb= requests.get(book).text
  soupb=bs.BeautifulSoup(sourceb,'lxml')
  elb=soupb.find_all("span",{"class":"js-subbuzz__title-text"})
  bookname=[]
  booklink=[]
  for i in elb[1:55]:
    a=i.find_all("a")
    bookname.append(a[0].contents[0])
    booklink.append(a[0]['href'])
  bookname[14]='Twilight Series'
  author=[]
  for j in elb[1:55]:
    b=j.contents
    if len(b)==2:
      author.append(b[1])
    else:
      author.append(' by J.K. Rowling')

  cover=[]
  fig=soupb.find_all("figure",{"class":"subbuzz__media"})
  for k in fig[1:55]:
    c=k.find_all("img")
    cover.append(c[0]['src'])

  n=random.randint(0,53)
  return bookname[n]+author[n], booklink[n], cover[n]

 