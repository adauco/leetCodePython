import requests
import bs4


result = requests.get("https://en.wikipedia.org/wiki/Guadalajara")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select("title")[0].text)

list = soup.select(".thumbimage")[0]
print(list['span'])
for l in list:
    print(l)


#for l in soup.select('.mw-headline'):
    # print(l.text)