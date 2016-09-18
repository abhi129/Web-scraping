import re
url=raw_input();
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
if(urls):
    for i in urls:
        j=re.split(':|//|/',i,2)
        Scheme=j[0]
        print "Scheme:",Scheme
        p=re.split('/',j[2],1)
        path=p[1]
        netloc=p[0]
        p1=re.split(':',netloc)
        port=p1[1]
        print "netloc:",netloc
        print "port:",port
        print "path:",path