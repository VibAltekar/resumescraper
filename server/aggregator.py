import PyPDF2 as pdf
import textract as extract
import re
from urllib.request import urlretrieve
from rake_nltk import Rake

r = Rake()


class Aggregator:
    def __init__(self, url):
        self.url = url
        self.tags = []
    def execute(self):
        urlretrieve(self.url, 'cv.pdf')
        dataObject = pdf.PdfFileReader('cv.pdf')
        self.fetchKeywords(dataObject)
        print (self.tags)
    def fetchKeywords(self, file):
        pages = file.numPages
        pg_count = 0
        return_text = ""
        while pg_count < pages:
            page = file.getPage(pg_count)
            pg_count += 1
            return_text += page.extractText()
        if return_text is not "":
            keywords = re.findall(r'[a-zA-Z]\w+',return_text)
            r.extract_keywords_from_sentences(keywords)
            sentences = r.get_ranked_phrases()
            self.tags = sentences
        return self.tags
