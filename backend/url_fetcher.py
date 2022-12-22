import requests
import re

urls = []
forbidden = ['.jpeg', '.jpg', '.svg', '.png', '.gif', '.css', '.js', '.mp4', '.mp3', '.wav', '.mov', '.woff'] # don't crawl image, movies, audio, font, or code files

def extract(res):
    regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    url = re.findall(regex,res)
    return [x[0] for x in url]

def verify(url):
    for extension in forbidden:
        if extension in url:
            return False
    return True

def update_urls(n, index): # n = number of urls to add

    desired_length = len(urls) + n

    # read
    f = open('urls.txt')
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        urls.append(line)

    # update
    while True:

        curr = urls[index]
        index += 1
        try:
            res = requests.get(curr).text
            found = extract(res)
            for url in found:
                if verify(url):
                    urls.append(url)

        except:
            continue

        if index == len(urls) or len(urls) >= desired_length:
            break
    
    # write
    f.close()
    f = open('urls.txt', 'w')
    for url in urls:
        f.write(url + '\n')