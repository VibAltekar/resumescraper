import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def download_res(url="https://vigneshp.com"):
    proc = os.popen("wget --no-directories --content-disposition -e robots=off -l1 -A.pdf -r " + str(url))
    return True

def extractMultipleLinks(collect=None):
    html_page = urlopen(collect)
    soup = BeautifulSoup(html_page)
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links

def fetchPDFfromLink(url=None):
    resource = None
    return resource


def main():
    listof_res = extractMultipleLinks("https://github.com/HackathonHackers/personal-sites")
    for res in listof_res:
        print (res)

if __name__ == '__main__':
    main()
    download_res()
