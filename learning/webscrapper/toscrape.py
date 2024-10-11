import requests
import bs4


def get_2star_titles():
    two_star_titles = []

    for i in range(1,20):
        base_url = "https://books.toscrape.com/catalogue/page-{}.html"
        res = requests.get(base_url.format(i))
        soup = bs4.BeautifulSoup(res.text, "lxml")

        books = soup.select(".product_pod")
        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                book_title = book.select('a')[1]['title']
                two_star_titles.append(book_title)
    print(two_star_titles)
    print(len(two_star_titles))

    return two_star_titles

def get_authors():
    url = 'http://quotes.toscrape.com/page/'
    authors = set()
    page_valid = True
    page = 1
    while page_valid:

        page_url = url+str(page)
        print(page_url)
        res = requests.get(page_url)
        if "No quotes found" in res.text:
            page_valid = False
        soup = bs4.BeautifulSoup(res.text, "lxml")
        for name in soup.select('.author'):
            authors.add(name.text)
        page = page + 1

    return authors


print(get_authors())
# get_2star_titles()





