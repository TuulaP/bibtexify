

# seek book's basic info from couple of search services
# create bibtex style copyable section for .bib file.

from finbooks import seekBookbyISBN
from string import Template

isbn = "9781784971618"
data = seekBookbyISBN(isbn)

#print(data)   #title, author, isbn, publisher, pubyear)

booktempl= Template('{@book{bookid, \n \
	author= {$author}, \n \
	title= {$title}, \n \
	publisher={$publisher}, \n \
	year= {$year}, \n \
    isbn= {$isbn} }') 

setup = dict(author= data[1],title = data[0], publisher=data[3],year=data[4],isbn = isbn )

result = booktempl.substitute(setup)

print(result)
