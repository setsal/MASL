import React, { Component } from 'react';
import '../../dist/homepage.css';
import logo from '../../dist/logo.png';
import Hero from "./Hero"

export default class Homepage extends Component {
    render() {
        return (
            <div>
                <Hero />
            <main id="main" className="site-main main">
            <title>MASL</title>
            <section className="hero">
                <div className="container">
                    <img src={logo}/>
                </div>
            </section>
            </main>
            </div>
        )
    }
}
