// import React from 'react';
// var React = require('react');
// var ReactDOM = require('react-dom/client');
// import ReactDOM from 'react-dom/client';
// import App from './App';
// var App = require("./App")

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// ReactDOM.render(<App />, document.querySelector('.app-mountpoint'))
'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return (
      <button onClick={() => this.setState({ liked: true })}>
        Like
      </button>
    );
  }
}
;
ReactDOM.render(<LikeButton />, document.querySelector('.app-mountpoint'));
// window.MyApp = {

//   init: function (opts) {
//     var mountPoint = document.querySelector(opts.el);

//     React.render(<App />, mountPoint);
//   }

// };
// import { createRoot } from 'react-dom/client';

// Clear the existing HTML content

// document.body.innerHTML = '<div id="app">Hello World!</div>';

// Render your React component instead
// const root = createRoot(document.getElementById('app'));
// root.render(<h1>Hello, world</h1>);
