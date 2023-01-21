query = "elon musk twitter"

var xhr = new XMLHttpRequest();
xhr.open("POST", "http://127.0.0.1:5000/search", false);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
    'query': query
}));

document.write(xhr.responseText)