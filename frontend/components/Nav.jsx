import React from "react"
import '../dist/nav.css';

export default class Nav extends React.Component {
    render() {
        return (
            <header className="header-area">
                <div className="container">
                    <div className="row">
                        <div className="col-12">
                            <nav className="navbar navbar-expand-lg">

                                <a className="navbar-brand" href="/"><img  alt="MASL"/></a>

                                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#worldNav" aria-controls="worldNav" aria-expanded="false" aria-label="Toggle navigation">
                                    <span className="navbar-toggler-icon"></span>
                                </button>

                                <div className="collapse navbar-collapse" id="worldNav">
                                    <ul className="navbar-nav ml-auto">
                                        <li className="nav-item active">
                                            <a className="nav-link" href="/">Home
                                                <span className="sr-only">(current)</span>
                                            </a>
                                        </li>
                                        <li className="nav-item dropdown">
                                            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Pages</a>
                                            <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                                <a className="dropdown-item" href="/">Home</a>
                                                <a className="dropdown-item" href="/">Catagory</a>
                                            </div>
                                        </li>
                                        <li className="nav-item">
                                            <a className="nav-link" href="/about/">About Us</a>
                                        </li>
                                        <li className="nav-item">
                                            <a className="nav-link" href="#">Sign In</a>
                                        </li>
                                        <li className="nav-item">
                                            <a className="nav-link" href="#">Sign Up</a>
                                        </li>
                                    </ul>

                                </div>
                            </nav>
                        </div>
                    </div>
                </div>
            </header>
        )
    }
}
