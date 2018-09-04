import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import SinglePost, { About, HotArticle } from './Catagory'


const Main = styled.main `
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


const kinds = [
    { "name": "kind1" },
    { "name": "kind2" },
    { "name": "kind3" },
    { "name": "kind4" },
];





export default class CatagoryContainer extends Component {

    render() {
        return (
            <div style={{
                'backgroundColor' : '#fff'
            }}>
            <title>Catagory</title>

            <Main>
                <div className="container">
                    <div className="row justify-content-center">
                        <div className="col-12 col-lg-8">
                            <SinglePost KindList = {kinds} />
                        </div>
                        <div className="col-12 col-md-8 col-lg-4">
                            {About}
                            {HotArticle}
                        </div>
                    </div>
                </div>
            </Main>
            </div>
        )}
}
