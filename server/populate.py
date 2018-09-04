from aggregator import Aggregator
import json
from bs4 import BeautifulSoup
import urllib.request as urllib2
import traceback

def fetchURLs():
    page = 'https://github.com/HackathonHackers/personal-sites/blob/master/README.md'
    try:
        content = urllib2.urlopen(page)
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find("article", { "class" : "markdown-body" }).find('ul').find_all('a')
        new_links = list(map(lambda x: x['href'], links))
        return new_links
    except urllib2.HTTPError as e:
        error('HTTPError = ' + str(e.code))
    except urllib2.URLError as e:
        error('URLError = ' + str(e.reason))
    except Exception:
        error('generic exception: ' + traceback.format_exc())

def fetchResumeResources():
    return ("")


def error(content):
    print (content)

print(fetchURLs())
