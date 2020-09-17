from urllib.request import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Process
import time

def crawl_url(browse_url):
    url = browse_url
    time.sleep(10)
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

def print_data(url=""):
    if(url):
        html = crawl_url(url)
        dt = clean_html(html)
        print(dt)
    else:
        print("Nothing to show...")

if __name__ == "__main__":
    
    urls = ["https://www.ebay.com/sch/i.html?_nkw=rtx+3080",
    "https://www.ebay.com/sch/i.html?_nkw=rtx+2080",
    "https://www.ebay.com/sch/i.html?_nkw=rtx+2060"]

    procs = []
    proc = Process(target=print_data)
    procs.append(proc)
    proc.start()

    for url in urls:
        proc = Process(target=print_data, args=(url,))
        procs.append(proc)
        proc.start()
    
    for process in procs:
        process.join()


