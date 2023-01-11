import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.css'
import SearchField from './components/searchField';
import Title from './components/title'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <br />
    <br />
    <br />
    <Title/>
    <br />
    <SearchField/>
  </React.StrictMode>
);