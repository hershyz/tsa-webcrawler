import requests
import re

urls = []
urls_set = set()
forbidden = ['.jpeg', '.jpg', '.svg', '.png', '.gif', '.css', '.js', '.php', '.mp4', '.mp3', '.wav', '.mov', '.woff'] # don't crawl image, movies, audio, font, or code files

def extract(res):
    regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    url = re.findall(regex,res)
    return [x[0] for x in url]

def verify(url):
    if url in urls_set:
        return False
    for extension in forbidden:
        if extension in url:
            return False
    return True

def update_urls(index): # n = number of urls to add

    # read
    f = open('urls.txt')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        urls.append(line)
        urls_set.add(line)

    # update
    curr = urls[index]
    try:
        res = requests.get(curr).text
        found = extract(res)
        for url in found:
            if verify(url):
                urls.append(url)
                urls_set.add(url)
    except:
        pass
    
    # write
    f.close()
    f = open('urls.txt', 'w')
    for url in urls:
        f.write(url + '\n')
    urls.clear()