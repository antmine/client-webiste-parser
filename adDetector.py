#!/usr/bin/env python2.7

#lib to query a website
import urllib2
#beautifulSoup4 lib to parse data from imported website
from bs4 import BeautifulSoup

from urllib import FancyURLopener
from random import choice

user_agents = [
   'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
   'Opera/9.25 (Windows NT 5.1; U; en)',
   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
   'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]

url1 = "http://www.jeuxvideo.com"
url2 = "http://puzl.com/fr"
url3 = "http://joinsquad.com/"
url4 = "https://stackoverflow.com"
url5 = "https://openclassrooms.com"

class MyOpener(FancyURLopener, object):
    version = choice(user_agents)

myOpener = MyOpener()
try:
    page = myOpener.open(url1)
    soup = BeautifulSoup(page, "html.parser")
    soup.prettify()
    if not soup.script.string:
        print "no ads"
    else:
        print "script balise present"
        if "ads" in soup.script.string:
            print "website contains ads"

except urllib2.HTTPError,e:
    print e.fp.read()
