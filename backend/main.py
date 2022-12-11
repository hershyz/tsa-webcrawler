# TODO: set up server routing

import url_fetcher

# test
url_fetcher.update_urls(1000)
for url in url_fetcher.urls:
    print(url)
print('current length: ' + str(len(url_fetcher.urls)))