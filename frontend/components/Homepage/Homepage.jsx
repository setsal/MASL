import React, { Component } from 'react';
import '../../dist/homepage.css';
import logo from '../../dist/logo.png';

export default class Homepage extends Component {
    render() {
        return (
            <main id="main" className="site-main main">
            <section className="hero">
                <div className="container">
                    <img src={logo}/>
                </div>
            </section>
            </main>
        )
    }
}
