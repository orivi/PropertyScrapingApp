import requests
from bs4 import BeautifulSoup


def scrape():
    pages = []
    l = []
    i = 0
    while i < 10:
        url = "https://www.ereality.cz/pronajem/byty/trebic?&ordr=&cena_od=0&cena_do=0&pg=0"
        new_url = list(url)
        new_url[-1] = str(i)
        new_page = "".join(new_url)
        pages.append(new_page)
        i = i+1
    for page in pages:
        page = requests.get(page)
        page = page.content
        soup = BeautifulSoup(page, "html.parser")
        ul = soup.find_all("ul", {"class": "ereality-property-list"})
        for tile in ul:

            tile = soup.find_all("li", {"class": "ereality-property-tile"})
            for item in tile:
                d = {}
                try:
                    heading = item.find(
                        "strong", {"class": "ereality-property-heading"}).text.split(",")[0:1]
                except:
                    None
                try:
                    d["location"] = item.find(
                        "p", {"class": "ereality-property-locality"}).text.split(",")[0]
                except:
                    d["location"] = None
                try:
                    d["price"] = item.find(
                        "div", {"class": "ereality-property-price"}).text.split("Kč")[0].replace(" ", "")
                except:
                    d["price"] = None
                for item in heading:
                    if item.find("+") != -1:
                        i = item.find("+")
                        d["size"] = item[i-1:i+3]

                    else:
                        d["size"] = "house"
                l.append(d)
    return l

