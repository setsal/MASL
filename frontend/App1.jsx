import React from "react"
import { render } from "react-dom"
import { Route, Switch, BrowserRouter, Link } from 'react-router-dom'
import styled from 'styled-components'

//import App1Container from "./containers/App1Container"
import Homepage from './components/Homepage/Homepage'
import About from './components/About/About'
import Footer from "./components/Footer"
import Catagory from "./components/Catagory/CatagoryContainer"
import NewsCatagory from "./components/Catagory/News/CatagoryContainer"
import Nav from "./components/Nav"
import FBCustomize from './components/Customize'
import FBResult from './components/Customize/CatagoryContainer'
import NewsCustomize from './components/Customize/News'
import NewsResult from './components/Customize/News/CatagoryContainer'
import 'semantic-ui-css/semantic.min.css'
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
                <Route path="/catagory" component={Catagory} />
                <Route path="/newscatagory" component={NewsCatagory} />

                <Route path="/fb_customize" component={FBCustomize} />
                <Route path="/fb_result" component={FBResult} />

                <Route path="/news_customize" component={NewsCustomize} />
                <Route path="/news_result" component={NewsResult} />
            <Footer />
        </Global>
        </BrowserRouter>
    )
  }
}

render( <App1/>, document.getElementById('App1') )
