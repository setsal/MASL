import React, { Component } from 'react';
import styled from 'styled-components';


const Main = styled.main`
    padding: 36px 0 47px;
`;



const Team = styled.div`
    padding: 0 0 72px;
`;



const IntroArticle = styled.article`
    border-top: 2px solid #8f8d87;
    padding: 27px 0 26px 2px;
    h1 {
        display: inline-block;
        vertical-align: middle;
        margin: 0 11% 0 0;
        width: 38.5%;
        text-transform: uppercase;
    }
    .box {
        display: inline-block;
        vertical-align: middle;
        width: 50%;
        font-size: 26px;
        line-height: 28px;
    }
`;


const Article = styled.article`
    overflow: hidden;
    position: relative;
    padding: 48px 30px 53px;
    border-top: 2px solid #8f8d87;
`;

const ImgBlock = styled.div`
    float: left;
`;

const ImgBlockInner = styled.div`
    overflow: hidden;
    display: block;
    position: relative;
    img {
        height: 50%;
        width: 59%;
        border-radius: 150px;
        margin-left: 100px;
        border: 2px solid #dbdbdb;
    }
`;

const TextBox = styled.div`
    h1 {
        text-transform: uppercase;
        margin: 90px 0 11px;
    }
    a {
        color: #4a4b4c;
    }
`;

const contributors = [
  {id: 1, name: 'setsal Lan', description: 'To be continue...', p_img: 'https://avatars0.githubusercontent.com/u/18705824?s=460&v=4', github: 'https://github.com/setsal' },
  {id: 2, name: 'setsal La2n', description: 'To be continue...', p_img: 'https://avatars0.githubusercontent.com/u/18705824?s=460&v=4', github: 'https://github.com/setsal' }
];

function Contributors(props) {
  const content = props.contributors.map((contributor) =>
    <div key={contributor.id}>
        <h3>{contributor.name}</h3>
      <h3>{contributor.description}</h3>
    </div>
  );
  return (
    <div>
      {content}
    </div>
  );
}

export default class About extends Component {
  render() {
    return (
        <Main className="container">
            <Team>
                <Article className="row">
                    <ImgBlock className="col-md-6">
                        <ImgBlockInner>
                            <img src="https://avatars0.githubusercontent.com/u/18705824?s=460&v=4" />
                        </ImgBlockInner>
                    </ImgBlock>

                    <TextBox className="col-md-6">
                        <h1>setsal Lan</h1>
                        <p>To be continue...</p>
                        <p><a href="https://github.com/setsal"><i className="fab fa-github fa-2x"></i></a></p>
                    </TextBox>
                </Article>
                <Article className="row">
                    <ImgBlock className="col-md-6">
                        <ImgBlockInner>
                            <img src="https://avatars0.githubusercontent.com/u/15828515?s=460&v=4" />
                        </ImgBlockInner>
                    </ImgBlock>

                    <TextBox className="col-md-6">
                        <h1>Meteor Hsu</h1>
                        <p>To be continue...</p>
                        <p><a href="https://github.com/ekids1234"><i className="fab fa-github fa-2x"></i></a></p>
                    </TextBox>
                </Article>
                <Article className="row">
                    <ImgBlock className="col-md-6">
                        <ImgBlockInner>
                            <img src="https://avatars3.githubusercontent.com/u/32054693?s=460&v=4" />
                        </ImgBlockInner>
                    </ImgBlock>

                    <TextBox className="col-md-6">
                        <h1>Andy Chu</h1>
                        <p>To be continue...</p>
                        <p><a href="https://github.com/CZ75auto"><i className="fab fa-github fa-2x"></i></a></p>
                    </TextBox>
                </Article>
                <Article className="row">
                    <ImgBlock className="col-md-6">
                        <ImgBlockInner>
                            <img src="https://avatars1.githubusercontent.com/u/40795118?s=460&v=4" />
                        </ImgBlockInner>
                    </ImgBlock>

                    <TextBox className="col-md-6">
                        <h1>Momo</h1>
                        <p>To be continue...</p>
                        <p><a href="https://github.com/ljk25679"><i className="fab fa-github fa-2x"></i></a></p>
                    </TextBox>
                </Article>
            </Team>
        </Main>
    )
  }
}
