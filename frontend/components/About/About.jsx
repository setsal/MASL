import React, { Component } from 'react';
import styled from 'styled-components';

const Team = styled.div`
  color: #4970B3;
`;

export default class About extends Component {
  render() {
    return (
        <main role="main" classNameName="container">
            <Team>
                <article className="box alignleft">

                    <div className="img-block">
                        <div className="img-box-inner">
                        <img src="" />
                        <div className="social-holder">
                            <ul className="social">
                                <li><a href=""><i className="fab fa-github"></i></a></li>
                            </ul>
                        </div>
                        </div>
                    </div>

                    <div className="text-box">
                        <h1>setsal Lan</h1>
                        <p>Some description</p>
                    </div>

                </article>
            </Team>
        </main>
    )
  }
}
