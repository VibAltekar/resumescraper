from aggregator import Aggregator
import json
from bs4 import BeautifulSoup
import urllib.request as urllib2
import urllib.parse
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
    all_urls = fetchURLs()
    resources = []
    for element in all_urls:
        e = {}
        e['url'] = element
        e['resource'] = fetchPDFSource(element)
        if e['resource'] is not None and e['resource'] is not "" and len(e['resource']) > 0:
            print(e)
            e['resource'] = list(set(e['resource']))
            resources.append(e)


def fetchPDFSource(url):
    try:
        content = urllib2.urlopen(url)
        soup = BeautifulSoup(content, 'html.parser')
        return (sniff(soup, url))
    except urllib2.HTTPError as e:
        error('HTTPError = ' + str(e.code))
    except urllib2.URLError as e:
        error('URLError = ' + str(e.reason))
    except Exception:
        error('generic exception: ' + traceback.format_exc())
    except timeout:
        error('Timeout')


def sniff(content, url):
    elements = []
    for link in content.find_all('a'):
        current_link = link.get('href')
        if current_link and current_link.endswith('pdf'):
            if current_link.startswith("http:"):
                dummy_current_link = current_link.lower()
                if "cv" in dummy_current_link or "resume" in dummy_current_link:
                    elements.append(current_link)
            else:
                dummy_current_link = current_link.lower()
                if "cv" in dummy_current_link or "resume" in dummy_current_link:
                    new_url = urllib.parse.urljoin(url, current_link)
                    elements.append(new_url)

    return elements



def error(content):
    print (content)

fetchResumeResources()
