#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Book data from finna by isbn, name

import urllib.request
#from urllib import urlopen
import pprint
import simplejson as json
# from booktogr import chkGoodReads
import sys

#from kitchen.text.converters import getwriter

url = "https://api.finna.fi/v1/search?lookfor="
CSVSEP = ";"
QUOTE = '"'
full = "&field[]=fullRecord"
recordurl = "https://api.finna.fi/v1/record?id="
suffix = "&field[]=id"
FLTR = "&filter[]=~"
booktype = '&filter[]=~format_ext_str_mv="1/Book/Book/"'
corefields="&field[]=publishers&field[]=publicationDates&field[]=publicationInfo&field[]=nonPresenterAuthors&field[]=title"

builcodes = {
    'helmet': 'building:"0/Helmet/"',
    'kaakkuri': 'building:"0/XAMK/"',
    'lumme': 'building:"0/Lumme/"',
}

marcfields = {
    'title': '245', 'author': '100',
    'publisher': '264', 'pubyear': '264',
    'isbn': '020'
}





def seekBookbyISBN(isbn, library="helmet"):

    library = builcodes[library]

    ##print("XXX", url+isbn+full+FLTR+library)

    result = urllib.request.urlopen(url+isbn+corefields).read() #+full+FLTR+library).read()
    result = json.loads(result)
    result = result.get('records')[0]

    #print("data searched:" + url + isbn + "\n")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(result)

    title = result['title']
    
    authors = result['nonPresenterAuthors']
    auths= []
    for auth in authors:
        if auth['role']=='kirjoittaja':
            auths.append(auth['name'])

    author = ", ".join(auths) # last first,_ as string
    publisher = ", ".join(result['publishers'])
    pubyear = result['publicationDates'][0] 

    #print("Valittu ISBN: {0}, title {1}".format(isbn, title.encode('utf-8')))

    return (title, author, isbn, publisher, pubyear)


#isbn = getFinnaRecord(ysid)
#print("ISBN: ", isbn)
# seekBookbyISBN("978-952-215-680-8")
