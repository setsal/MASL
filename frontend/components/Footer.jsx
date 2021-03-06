import React from "react"
import '../dist/footer.css';

export default class Footer extends React.Component {
    render() {
        return (
            <footer className="footer">
            <div className="container">
                <div className="footer__inner">
                    <div className="footer__item d-lg-flex justify-content-lg-between align-items-lg-center">
                        <ul id="menu-footer" className="nav sub-nav footer__sub-nav">
                            <li id="menu-item-119" className="menu-item menu-item-type-post_type menu-item-object-page menu-item-119">
                                <a title="Terms of Service" href="/about/">About US</a>
                            </li>
                        </ul>
                        <p className="hidden-sm-down d-none d-lg-block"> Spread the creating !</p>
                    </div>
                </div>
            </div>
            </footer>
        )
    }
}
