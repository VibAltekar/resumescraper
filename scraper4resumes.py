import os
import sys
from bs4 import BeautifulSoup

from urllib.request import urlopen
import re


def download_res(url="https://vigneshp.com"):
    #if url[0:3] != "http":
        #url = "http://" + url
    proc = os.popen("wget --no-directories --content-disposition -e robots=off -l1 -A.pdf -r " + str(url))
    #proc.readlines()
    return True

def getLinks(url="https://github.com/HackathonHackers/personal-sites"):
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        links.append(link.get('href'))
    return links


def main():
    listof_res = getLinks()
    for res in listof_res:
        download_res(res)

if __name__ == '__main__':
    main()

