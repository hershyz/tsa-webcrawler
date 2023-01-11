import React, { Component } from 'react';

class searchField extends Component {

    state = {
        searchResults: ['babbb']
    }

    search = () => {
        
        // call api here:

        this.setState({
            searchResults: ['wabb', 'dabbbb'] // placeholder
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
                    <input placeholder="Query..." className="form-control" style={{width: "600px"}}/>
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