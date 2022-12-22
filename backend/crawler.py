import url_fetcher
import time

index = 0
while True:
    url_fetcher.update_urls(100, index)
    index += 1
    print('cycles: ' + str(index))
    time.sleep(5)