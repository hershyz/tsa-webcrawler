import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.css'
import SearchField from './components/searchField';
import HeadingText from './components/headingText';
import Results from './components/results'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
  <HeadingText/>
  <SearchField/>
  <Results/>
  </React.StrictMode>
);