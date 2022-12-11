# TODO: set up server routing

import url_fetcher

url_fetcher.update_urls(100)
urls = url_fetcher.urls

for url in urls:
    print(url)

print('current length: ' + str(len(urls)))