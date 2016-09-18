from lxml import html
import requests
import HTMLParser
import urllib
from BeautifulSoup import BeautifulSoup
def scrap(keyword1,url):
    url.replace(keyword,keyword1)
    result= urllib.urlencode(url)
    results1=result.read()
    soup = BeautifulSoup(results1)
    soup1=soup.select('results')
    n=int(len(soup1))
    print(n)
def scrap1(keyword1,pageno,url):
    url=raw_input()
    url.replace(keyword,keyword1)
    url.replace(number,pageno)
    try:
        result= urllib.urlencode(url)
    except:
        print("page not found")
    else:
        results1=result.read()
        soup = BeautifulSoup(results1)
        soup1=soup.select('results')
        dict={}
        d1={}
        for  i in range(len(soup1)):
            d['type']=type(soup1[0])
            d['text']=soup1[0].getText()
            d['attributes']=soup1[0].attrs
            dict[i]=d
            d.clear()
        print(dict)
print("Enter url")
url1=input()
print "Enter query number "
query=input()
print("Enter keyword")
keyword=input()
if(query==1):
    scrap(keyword,url1)
if(query==2):
    print("enter page number")
    pagenumber=input()
    soup1(keyword,pagenumber,url1)
    

            
            
            
    
    
    





