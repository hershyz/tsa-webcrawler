from flask import Flask, request
from flask_cors import CORS
import search

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'search server is active'

@app.route('/search', methods=['POST'])
def search_endpoint():

    data = request.json
    print(data)
    query = str(data['query'])
    res = str(search.search(query))
    return res

if __name__ == "__main__":
    app.run()