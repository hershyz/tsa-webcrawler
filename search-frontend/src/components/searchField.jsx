import React, { Component } from 'react';

class searchField extends Component {
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