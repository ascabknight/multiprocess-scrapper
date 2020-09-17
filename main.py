from urllib.request import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Process

def crawl_url(browse_url):
    url = browse_url
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    tags = soup.find_all("h3", class_="s-item__title")
    names = []
    for tag in tags:
        tag = tag.find(text=True, recursive=False)
        names.append(tag)
    return names

def print_data(url):
    html = crawl_url(url)
    dt = clean_html(html)
    print(dt)

if __name__ == "__main__":
    url = "https://www.ebay.com/sch/i.html?_nkw=rtx+3080"
    print_data(url)


