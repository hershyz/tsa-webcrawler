import hashlib
import page_parser

def index(url):
    
    words = page_parser.parse(url)

    for word in words:

        m = hashlib.sha256()
        m.update(word.encode('utf-8'))
        res = m.hexdigest()

        '''
            todo:
            - create backend/db dir
            - check if 'res' exists in db
                if it does, append url to 'res'
                if it doesn't, create 'res' and apend url
        '''