// import React from 'react';
// var React = require('react');
// var ReactDOM = require('react-dom/client');
// import ReactDOM from 'react-dom/client';
const ads_json = [
  {
    "ad_type": "sell",
    "text": "selling bike", "user": "bob", "date": "1/20/2023"
  },
  {
    "ad_type": "buy",
    "text": "buy car", "user": "eric", "date": "4/23/2023"
  }
]


function Filterable_Ads() {
  const [ad_type, adtype_changer] = React.useState("BuyOrSell")
  const [search_text, search_text_changer] = React.useState("")
  return (
    <div className='filterable_ads'>
      <AdType_Selector changer={adtype_changer} />
      <SearchBar changer={search_text_changer} />
      <AdsList ads={ads_json} ad_type={ad_type} search_text={search_text} />
    </div>
  )

}

function AdType_Selector({ changer }) {

  return (
    <div className='adtype_selector'>
      <select onChange={(event) => changer(event.target.value)}>
        <option value="BuyOrSell">Buy or Sell</option>
        <option value="Buy">Buy</option>
        <option value="Sell">Sell</option>
      </select>
    </div >
  )

}

function SearchBar({ changer }) {
  return (
    <div className='search_bar'>
      <label>Search:</label>
      <input type="text" onChange={(event) => changer(event.target.value)}></input>
    </div>
  )

}

function AdsList({ ads, ad_type, search_text }) {

  function ad_filter(ad) {
    return ((ad_type.toUpperCase() == "BuyOrSell".toUpperCase() ||
      ad_type.toUpperCase() == ad.ad_type.toUpperCase()) &&
      (search_text == "" || ad.text.includes(search_text)))
  }


  let ads_filtered = ads.filter((ad) => ad_filter(ad))
  function ad_json_unpacker(ad) {
    return ad.ad_type + ": " + ad.text + ". Posted by " + ad.user + " on " + ad.date
  }
  function ad_json_key(ad) {
    return ad.user + ad.text
  }
  let lis = ads_filtered.map((item) => <li key={ad_json_key(item)}>{ad_json_unpacker(item)}</li>)
  return (
    <div className='ads_list'>
      <ul>{lis}</ul>
    </div>
  )

}


function App() {
  return (
    <Filterable_Ads />
  );
}
// import App from './App.js';
// var App = require("./App")

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

ReactDOM.render(<App />, document.querySelector('.app-mountpoint'))
'use strict';


// import { createRoot } from 'react-dom/client';

// Clear the existing HTML content

// document.body.innerHTML = '<div id="app">Hello World!</div>';

// Render your React component instead
// const root = createRoot(document.getElementById('app'));
// root.render(<h1>Hello, world</h1>);
