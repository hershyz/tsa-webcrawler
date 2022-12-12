import requests
import re

urls = ['https://www.theverge.com']
last_index = [-1]

def extract(res):
    regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    url = re.findall(regex,res)
    return [x[0] for x in url]

def update_urls(n): # n = number of urls to add

    desired_length = len(urls) + n

    # update
    index = last_index[0] + 1
    while True:

        curr = urls[index]
        index += 1
        try:
            res = requests.get(curr).text
        except:
            continue
        found = extract(res)
        for url in found:
            if '.jpeg' not in url and '.jpg' not in url and '.svg' not in url and '.png' not in url: # don't crawl image files
                urls.append(url)

        if index == len(urls) or len(urls) >= desired_length:
            last_index[0] = index
            break