import React from "react"
import { render } from "react-dom"
import { Route, Switch, BrowserRouter, Link } from 'react-router-dom';

//import App1Container from "./containers/App1Container"
import Homepage from './components/Homepage/Homepage';
import Footer from "./components/Footer"
import Nav from "./components/Nav"
import './dist/style.css'

class App1 extends React.Component {
  render() {
    return (
        <BrowserRouter>
        <div>
            <Nav />
                <Route path="/" component={Homepage} exact/>
            <Footer />
        </div>
        </BrowserRouter>
    )
  }
}

render( <App1/>, document.getElementById('App1') )
