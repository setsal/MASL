import React, { Component } from 'react';
import styled from 'styled-components';
import { Container, Divider, Grid, Header, Segment, Icon } from 'semantic-ui-react'


const Main = styled.main`
    padding: 36px 0 47px;
    text-align: center;
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
    cursor: pointer;
`
const Jumbotron = styled.section`
    text-align: center;
    background: #98ddf5;
    .mission {
        font-weight: 300
    }
`

export default class About extends Component {

    constructor(props) {
        super(props);
        this.state = {
            authorlist: [
                {
                    name: "setsal Lan", pic: "https://avatars0.githubusercontent.com/u/18705824?s=460&v=4", descption: "似乎是雜食菜吃多了, 又或是這五光十色的社會所迷惘, 腦中想的, 總沒有個好想法"
                }, {
                    name: "Momo Zhang", pic: "https://avatars0.githubusercontent.com/u/40795118?s=460&v=4", descption: "資訊工程學系 大四 卷哥大大"
                }, {
                    name: "MeteorV Hsu", pic: "https://avatars0.githubusercontent.com/u/15828515?s=460&v=4", descption: "資訊工程學系 大四 最渣的 無法克制自己"
                }, {
                    name: "Andy Chu", pic: "https://avatars0.githubusercontent.com/u/32054693?s=460&v=4", descption: "資訊工程學系 大四 也是大大"
                }]
        }
    }
    toggleHover() {
        this.setState({ hover: true });
        if (this.state.hover) {
            linkStyle = { backgroundColor: 'red', color: inherit }
            console.log("QQ");

        }
    }


    render() {

        /*
        const custom_card_style = styled.custom-card`
            :hover{color: inherit;}
        `;
        */


        let DOM = this.state.authorlist.map((author) =>
            (

                <Personal className="col-xxs-12 col-sm-6 col-xxl-3 m-b-xxl" data-toggle="modal" data-target={"#" + author.name + "ModalCenter"}>
                <PersonalIMG className="img-circle img-fluid mx-auto m-b" src={author.pic} />
                <h3 className="text-md text-bold">{author.name}</h3>
                <p className="text-xxs mb-2 text-uppercase">Programer</p>
                <p className="description mx-auto">
                    {author.descption}
                </p>

                {/* Modal */}
                <div className="modal fade" id={author.name + "ModalCenter"} tabIndex="-1" role="dialog" aria-labelledby={author.name + "CenterTitle"} aria-hidden="true">
                    <div className="modal-dialog modal-dialog-centered" role="document">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title" id={author.name + "ModalLongTitle"}>{author.name+ " Introduction"}</h5>
                                <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div className="modal-body">
                                大家都覺得{author.name == "MeteorV Hsu" ? author.name+"像個渣" : author.name+"是大大"}
                            </div>
                            <div className="modal-footer">
                                <button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
                                <button type="button" className="btn btn-primary" >讚ㄛ </button>
                            </div>
                        </div>
                    </div>
                </div>

            </Personal>
            )
        )

        return (
            <div style={{

            }}>
                <title>About US</title>

                <Main>
                    <Container>
                        <style>{`
                          p > span {
                            opacity: 0.4;
                            text-align: center;
                          }
                        }
                        `}</style>
                        <Grid.Row>
                            <div className="col-xxs-12 col-lg-10 mx-auto">
                                    <Segment>
                                        <Header as='h2' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                          Leadership
                                        </Header>
                                        <Grid.Row>
                                            {DOM}
                                        </Grid.Row>
                                    </Segment>
                            </div>
                        </Grid.Row>
                    </Container>
                </Main>
            </div>
        )
    }
}
