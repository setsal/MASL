import React from "react"

import Headline from "../components/Headline"
import Homepage from "../components/Homepage"
import Nav from "../components/Nav"
import Footer from "../components/Footer"

export default class App1Container extends React.Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Homepage></Homepage>
          </div>
        </div>
      </div>
    )
  }
}
