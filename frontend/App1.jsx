import React from "react"
import { render } from "react-dom"
import { Route, Switch, BrowserRouter, Link } from 'react-router-dom';
import styled from 'styled-components';

//import App1Container from "./containers/App1Container"
import Homepage from './components/Homepage/Homepage';
import About from './components/About/About';
import Footer from "./components/Footer"
import Nav from "./components/Nav"
import './dist/style.css'


const Global = styled.div `
    font-family: 'Noto Sans TC', sans-serif;
`;


class App1 extends React.Component {
  render() {
    return (
        <BrowserRouter>
        <Global>
            <Nav />
                <Route path="/" component={Homepage} exact/>
                <Route path="/about" component={About} />
            <Footer />
        </Global>
        </BrowserRouter>
    )
  }
}

render( <App1/>, document.getElementById('App1') )
