import hashlib
from os.path import exists

def search(text):

    words = text.split(' ')
    for i in range(len(words)):
        words[i] = words[i].lower()

    # key = url, value = freq
    res = {}

    for word in words:
        
        m = hashlib.sha256()
        m.update(word.encode('utf-8'))
        hash = m.hexdigest()

        if exists('db/' + str(hash)):
            f = open('db/' + str(hash), 'r')
            lines = f.readlines()
            for url in lines:
                url = url.replace('\n', '')
                if url in res:
                    res[url] = res[url] + 1
                if url not in res:
                    res[url] = 1

    res = sorted(res.items(), key=lambda x:x[1], reverse=True) # turns the dict into an array of tuples
    urls = []
    for element in res:
        urls.append(element[0])
    return urls