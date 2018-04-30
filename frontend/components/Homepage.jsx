import React from "react"
import '../dist/homepage.css';
import logo from '../dist/logo.png';

export default class Homepage extends React.Component {
    render() {
        return (
            <main id="main" class="site-main main">
            <section class="hero">
                <div class="container">
                    <img src={logo} />
                </div>
            </section>
        </main>)
    }
}
