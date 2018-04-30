import React from "react"
import { render } from "react-dom"

import App1Container from "./containers/App1Container"
import Footer from "./components/Footer"
import Nav from "./components/Nav"
import './dist/style.css'

class App1 extends React.Component {
  render() {
    return (
        <div>
            <Nav />
            <App1Container />
            <Footer />
        </div>
    )
  }
}

render( <App1/>, document.getElementById('App1') )
