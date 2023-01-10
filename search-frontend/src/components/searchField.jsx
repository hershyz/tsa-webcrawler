import React, { Component } from 'react';

class searchField extends Component {

    // search() {
    //     const results = [];
    //     results[0] = 'Test Result 1';
    //     results[1] = 'Test Result 1';
    //     results[2] = 'Test Result 1';
    //     TODO: wat do i do wit dis
    // }

    render() {
        return (
            <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
            }}>
                <input placeholder="Query..." className="form-control" style={{width: "600px"}}/>
                <button type="button" className="btn btn-dark m-2">Search</button>
            </div>
        )
    }
}

export default searchField;