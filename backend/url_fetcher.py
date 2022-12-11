import requests
import re
urls = ['https://www.youtube.com']

def extract(res):
    regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    url = re.findall(regex,res)      
    return [x[0] for x in url]

def update_urls(n): # n = number of urls to add
    
    # TODO: make urls array populate from a database

    desired_length = len(urls) + n

    index = 0
    while True:

        curr = urls[index]
        index += 1
        try:
            res = requests.get(curr).text
        except:
            continue
        found = extract(res)
        for url in found:
            urls.append(url)

        if index == len(urls) or len(urls) >= desired_length:
            break