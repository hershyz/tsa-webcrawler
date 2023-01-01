import hashlib
import page_parser
from os.path import exists

def index(url):
    
    words = page_parser.parse(url)
    for word in words:

        # hash word
        m = hashlib.sha256()
        m.update(word.encode('utf-8'))
        hash = m.hexdigest()

        # create word entry in db if it doesn't exist
        if not exists('db/' + str(hash)):
            f = open('db/' + str(hash), 'x')
        
        # append url to the document if it isn't already present inside
        f = open('db/' + str(hash), 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
        if url not in lines:
            f = open('db/' + str(hash), 'a')
            f.write(url + '\n')




# run sequence (convert to function later)
f = open('urls.txt', 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

for url in lines:
    print('caching \'' + url + '\'')
    index(url)