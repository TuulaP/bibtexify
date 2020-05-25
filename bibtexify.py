

# seek book's basic info from couple of search services
# create bibtex style copyable section for .bib file.

from finbooks import seekBookbyISBN
from string import Template


def bibtexifyISBN(isbn):
    data = seekBookbyISBN(isbn)

    # print(data)   #title, author, isbn, publisher, pubyear)
    if (data):
        booktempl = Template('{@book{bookid, \n \
            author= {$author}, \n \
            title= {$title}, \n \
            publisher={$publisher}, \n \
            year= {$year}, \n \
            isbn= {$isbn} }')

        setup = dict(author=data[1], title=data[0],
                     publisher=data[3], year=data[4], isbn=isbn)

        result = booktempl.substitute(setup)
    else:
        result = None

    return result


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description='From isbn to bibtex')
    parser.add_argument("-i", "--isbn", dest="isbn",
                        help="add individual isbn to reading list")

    args = parser.parse_args()
    books = []

    print("Isbn: ", args.isbn)
    isbn = args.isbn

    if args.isbn is None:
        print("Please give valid isbn")
        isbn = "9781784971618"

    else:
        result = bibtexifyISBN(isbn)

        if result is not None:
            print(result)
        else:
            print("Sorry, no book found with isbn: {0}".format(isbn))

