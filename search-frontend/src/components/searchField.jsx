import React, { Component } from 'react';

class searchField extends Component {

    state = {
        searchResults: ['[placeholder]']
    }

    search = () => {
        
        var query = document.getElementById('searchBox').value;

        // call api here:

        this.setState({
            searchResults: query.split(' ') // placeholder demo code
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
                    <input id="searchBox" placeholder="Query..." className="form-control" style={{width: "600px"}}/>
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