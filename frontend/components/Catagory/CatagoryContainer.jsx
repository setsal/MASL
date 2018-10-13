import React, {Component} from 'react';
import axios from 'axios';
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
    {
      "kind": "topic0",
      "articles":
        [
            {
              "title": "topic0-Title0",
              "content": "topic0-Content0"
            },
            {
                "title": "topic0-Title1",
                "content": "topic0-Content1"
            },
        ]
    },
    {
      "kind": "topic1",
      "articles":
        [
            {
              "title": "topic1-Title0",
              "content": "topic1-Content0"
            },
            {
                "title": "topic1-Title1",
                "content": "topic1-Content1"
            },
            {
                "title": "topic1-Title1",
                "content": "topic1-Content1"
            },
        ]
    }

];


export default class CatagoryContainer extends Component {
    constructor(props) {
      super(props);
        this.state = {
            topics: [],
        };
    }

    async componentDidMount() {
      /*
      axios.get('http://localhost:8000/getCluster/')
      .then( res => {
          const articles = res.data;
          this.setState({ articles });
      })
      */
      try {
        const res = await fetch('http://localhost:8000/cluster/');
        const topics = await res.json();
        this.setState({
          topics
        });
      } catch (e) {
        console.log(e);
      }
    }

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
                            <SinglePost topics={this.state.topics} />
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
