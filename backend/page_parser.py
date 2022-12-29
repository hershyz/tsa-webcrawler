import requests
import html2text

def parse(url):
    raw = requests.get(url).text
    h = html2text.HTML2Text()
    h.ignore_links = False
    return h.handle(raw)