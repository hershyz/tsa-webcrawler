import React, { Component } from 'react';

class searchField extends Component {

    state = {
        searchResults: []
    }

    search = async () => {
        
        await new Promise(r => setTimeout(r, 1000)); // don't overload the backend
        var query = document.getElementById('searchBox').value;

        // call api
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:5000/search", false);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            'query': query
        }));

        // format response
        var rawResponse = xhr.responseText;
        rawResponse = rawResponse.replace(/["']/g, "");
        rawResponse = rawResponse.replace('[', '');
        rawResponse = rawResponse.replace(']', '');

        this.setState({
            searchResults: rawResponse.split(', ')
        })
    }

    buildResults = () => {
        var innerPre = "";
        for (var i = 0; i < this.state.searchResults.length; i++) {
            innerPre += this.state.searchResults[i] + "\n"
        }
        return innerPre;
    };

    render() {
        return (
            <div>
                <div style={{
                    display: 'flex',
                    justifyContent:'center',
                    alignItems:'center',
                }}>
                    <input id="searchBox" placeholder="Query..." className="form-control" style={{width: "600px"}} onChange={ this.search }/>
                    <button type="button" className="btn btn-dark m-2" onClick={ this.search }>Search</button>
                </div>
                <br />
                <div style={{textAlign: 'center'}}>
                <pre>
                    { this.buildResults() }
                </pre>
                </div>
            </div>
        )
    }
}

export default searchField;