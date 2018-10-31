import React, {Component} from 'react';
import axios from 'axios';
import styled from 'styled-components';
import '../../../dist/catagory.css';
import SinglePost, { About, HotArticle } from './Catagory'
import Modal from "react-responsive-modal";

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

const contentStyle = {
    whiteSpace: 'pre-line'
}


export default class CatagoryContainer extends Component {
    constructor(props) {
      super(props);
        this.state = {
            topics: [],
            content: [],
            title: [],
            open: false,
        };

        this.onOpenModal = this.onOpenModal.bind(this);
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
        const res = await fetch('http://localhost:8000/news_cluster/');
        const topics = await res.json();
        this.setState({
          topics
        });
      } catch (e) {
        console.log(e);
      }
    }

    onOpenModal(letter, letter2) {
      this.setState ({
          open: true,
          content: letter,
          title: letter2
      });
    }

    onCloseModal = () => {
      this.setState({ open: false });
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
                            <SinglePost
                                topics={this.state.topics}
                                open={this.state.open}
                                onOpenModal={this.onOpenModal}
                                onCloseModal={this.onCloseModal}
                            />
                        </div>
                        <div className="col-12 col-md-8 col-lg-4">
                            {About}
                            {HotArticle}
                        </div>
                    </div>
                </div>
                <Modal open={this.state.open} onClose={this.onCloseModal} center>
                    <h2>{this.state.title}</h2>
                    <p style={ contentStyle }>
                      {this.state.content}
                    </p>
                </Modal>
            </Main>
            </div>
        )}
}