import React from "react"
import '../dist/nav.css';

export default class Nav extends React.Component {
    render() {
        return (<nav className="navbar navbar-expand-lg navbar-light">
            <div className="container">
                <a href="/" className="navbar-brand">MASL Project</a>
                <div className="d-flex ml-auto">
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#globalNavbar" aria-controls="globalNavbar" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                </div>
                <div className="collapse navbar-collapse" id="globalNavbar">

                    <ul className="navbar-nav mr-auto order-1">
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" id="navbarDropdownMenuLink" href="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Menu</a>
                            <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                <div className="navbar-collapse navbar-top-collapse">
                                    <ul id="menu-top-menu" className="nav navbar-nav">
                                        <li id="menu-item-601" className="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-601">
                                            <a title="" href="">Categories</a>
                                        </li>
                                        <li id="menu-item-603" className="menu-item menu-item-type-taxonomy menu-item-object-product_cat menu-item-603">
                                            <a title="" href="">Corporate</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="/about/">About</a>
                        </li>
                    </ul>
                    <ul className="navbar-nav d-none d-lg-flex ml-2 order-3">
                        <li className="nav-item">
                            <a className="nav-link" href="">Sign in</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="">Sign up</a>
                        </li>
                    </ul>
                    <ul className="navbar-nav d-lg-none">
                        <li className="nav-item-divider"></li>
                        <li className="nav-item">
                            <a className="nav-link" href="">Sign in</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="">Sign up</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>)
    }
}
