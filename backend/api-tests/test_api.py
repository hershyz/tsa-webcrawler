import requests

payload = {
    'query': 'apple m1 macbook pro air'
}

r = requests.post('http://127.0.0.1:5000/search', json=payload)
print(r.text)