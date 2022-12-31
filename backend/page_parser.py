import requests
import html2text

def parse(url):
    
    # parse into a single string
    raw = requests.get(url).text
    h = html2text.HTML2Text()
    h.ignore_links = False

    # convert to lowercase
    arr = h.handle(raw).split(' ')
    for i in range(len(arr)):
        arr[i] = arr[i].lower()
    
    return arr

print(parse('https://www.pornhub.com'))