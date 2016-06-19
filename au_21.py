#!/usr/bin/python
import urllib
#import urllib2
from urllib.request import urlopen
print ("au_started") # ne importiruet sobsks
#response = urllib2.urlopen('http://python.org/')
response = urlopen('http://python.org/')
html1 = response.read()
print(html1) 
print ("au ended1")
print (str(5))
mf=open('f2.txt','w')
mf.write(str(html1))
mf.close() 
print ("au ended2")