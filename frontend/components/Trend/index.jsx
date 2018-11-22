import React, { Component } from 'react';
import styled from 'styled-components';
import { Container, Header, Segment } from 'semantic-ui-react'
import Slider from "react-slick";
import { Grid } from 'semantic-ui-react'
import { Sep_e, Sep_l, Oct_e, Oct_l, Nov_e } from './Static'
import WordCloud from "react-d3-cloud";

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

const data = [
  { text: "Hey", value: 1000 },
  { text: "lol", value: 200 },
  { text: "first impression", value: 800 },
  { text: "very cool", value: 1000000 },
  { text: "duck", value: 10 }
];
const fontSizeMapper = word => Math.log2(word.value) * 10;
const rotate = word => word.value % 360;
const picwidth = 1000;
const picfont = "Noto Sans TC"

class NewTrend extends Component {

    constructor(props) {
        super(props);
        this.state = {
            isLoading: true
        }
    }

    render() {
        var settings = {
          dots: false,
          infinite: true,
          autoplaySpeed: 6000,
          slidesToShow: 1,
          autoplay: true,
          arrows: false,
        };
        return (
            <div style={{
                marginBottom: '50px'
            }}>
                <title>新聞趨勢</title>

                <Main>
                    <Container>
                        <Header as='h2' textAlign='center' style={{ marginTop: '1.2rem'}}>
                            新聞趨勢
                        </Header>
                        <Grid verticalAlign='middle' centered>
                            <Grid.Row>
                            <Grid.Column>
                            <Segment style={{ maxWidth: '1200px'}}>
                                <Slider {...settings} >
                                    <div>
                                        <WordCloud width={picwidth} font={picfont} data={Sep_e} fontSizeMapper={fontSizeMapper} rotate={rotate} />
                                        <Header as='h3' textAlign='center' style={{ marginTop: '1.2rem', verticalAlign: 'baseline'}}>
                                                9月收斂自詞
                                        </Header>
                                    </div>
                                    <div>

                                            <WordCloud width={picwidth} font={picfont} data={Sep_l} fontSizeMapper={fontSizeMapper} rotate={rotate} />
                                        <Header as='h3' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                            10月初收斂自詞
                                        </Header>

                                    </div>
                                    <div>

                                        <WordCloud width={picwidth} font={picfont} data={Oct_e} fontSizeMapper={fontSizeMapper} rotate={rotate} />
                                        <Header as='h3' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                            10月末收斂自詞
                                        </Header>

                                    </div>
                                    <div>

                                            <WordCloud width={picwidth} font={picfont} data={Oct_l} fontSizeMapper={fontSizeMapper} rotate={rotate} />
                                        <Header as='h3' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                            10月末收斂自詞
                                        </Header>
                                    </div>
                                    <div>

                                            <WordCloud width={picwidth} font={picfont} data={Nov_e} fontSizeMapper={fontSizeMapper} rotate={rotate} />
                                        <Header as='h3' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                            11月初收斂自詞
                                        </Header>

                                    </div>
                                </Slider>
                            </Segment>
                        </Grid.Column>
                        </Grid.Row>
                        </Grid>
                    </Container>
                </Main>
            </div>
        )
    }
}

export default NewTrend
