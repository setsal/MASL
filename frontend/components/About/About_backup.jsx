import React, { Component } from 'react';
import styled from 'styled-components';

const Main = styled.main`
    padding: 36px 0 47px;
    h2 {
        font-weight: 300;
        font-size: 32px;
        line-height: 1.25;
        margin-bottom: 5rem;
        margin-top: 2rem;
    }
    .container {
        margin-top: 80px;
    }
`;

const PersonalIMG = styled.img`
    margin-bottom: 1.5rem;
    width: 114px;
    border-radius: 50%;
    display: block;
    max-width: 100%;
    height: auto;
`

const Personal = styled.div`
    margin-bottom: 5rem;
    .text-md {
        font-size: 20px;
    }
    .text-xxs {
        font-size: 12px;
    }
    .description {
        max-width: 20rem;
        font-size: 16px;
    }
`
const Jumbotron = styled.section`
    text-align: center;
    background: #98ddf5;
    .mission {
        font-weight: 300
    }
`

export default class About extends Component {
    render() {
        return (

            <div style={{
                'backgroundColor': '#b6c1d9'
            }}>
                <title>About US</title>

                <Main>
                    <div className="container">
                        <div className="row">
                            <div className="col-xxs-12 col-lg-10 mx-auto">
                                <div className="row">
                                    <section className="card card-lg p-b-0 text-xxs-center" id="about-leadership">
                                        <h2>Leadership</h2>

                                        <div className="row">
                                            <Personal className="col-xxs-12 col-sm-6 col-xxl-3 m-b-xxl">
                                                <PersonalIMG className="img-circle img-fluid mx-auto m-b" src="https://avatars0.githubusercontent.com/u/18705824?s=460&v=4" />
                                                <h3 className="text-md text-bold">setsal Lan</h3>
                                                <p className="text-xxs mb-2 text-uppercase">Programer</p>
                                                <p className="description mx-auto">
                                                    似乎是雜食菜吃多了, 又或是這五光十色的社會所迷惘, 腦中想的, 總沒有個好想法
                                                </p>
                                            </Personal>
                                            <Personal className="col-xxs-12 col-sm-6 col-xxl-3 m-b-xxl">
                                                <PersonalIMG className="img-fluid mx-auto m-b" src="https://avatars1.githubusercontent.com/u/40795118?s=460&v=4" />
                                                <h3 className="text-md text-bold">Momo Zhang</h3>
                                                <p className="text-xxs mb-2 text-uppercase">Programer</p>
                                                <p className="description mx-auto">資訊工程學系 大四 卷哥大大</p>
                                            </Personal>
                                            <Personal className="col-xxs-12 col-sm-6 col-xxl-3 m-b-xxl">
                                                <PersonalIMG className="img-fluid mx-auto m-b" src="https://avatars0.githubusercontent.com/u/15828515?s=460&v=4" />
                                                <h3 className="text-md text-bold">MeteorV Hsu</h3>
                                                <p className="text-xxs mb-2 text-uppercase">Programer</p>
                                                <p className="description mx-auto">資訊工程學系 大四 最渣的 無法克制自己</p>
                                            </Personal>
                                            <Personal className="col-xxs-12 col-sm-6 col-xxl-3 m-b-xxl">
                                                <PersonalIMG className="img-fluid mx-auto m-b" src="https://avatars3.githubusercontent.com/u/32054693?s=460&v=4" />
                                                <h3 className="text-md text-bold">Andy Chu</h3>
                                                <p className="text-xxs mb-2 text-uppercase">Programer</p>
                                                <p className="description mx-auto">資訊工程學系 大四 也是大大</p>
                                            </Personal>
                                        </div>

                                    </section>

                                </div>
                            </div>
                        </div>
                    </div>
                </Main>
            </div>
        )
    }
}
