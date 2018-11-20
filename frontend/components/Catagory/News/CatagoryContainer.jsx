import React, {Component} from 'react';
import axios from 'axios';
import styled from 'styled-components';
import '../../../dist/catagory.css';
import SinglePost, { About, HotArticle } from './Catagory'
import TopicCloud from '../TopicCloud'
import Modal from "react-responsive-modal";
import {Dimmer, Loader, Segment} from 'semantic-ui-react'

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
    .single_post {
        text-align: left;
        white-space: pre-line;
    }
    .widget-content {
        line-height: 1.5;
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
            keywords: [],
            open: false,
            isLoading: false,
        };

        this.onOpenModal = this.onOpenModal.bind(this);
        this.changeKeywords = this.changeKeywords.bind(this);
    }

    async componentDidMount() {
      try {
        this.setState({
             isLoading: true
        });
        const res = await fetch('http://localhost:8000/news_cluster/');
        const topics = await res.json();
        this.setState({
          topics,
          isLoading: false
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

    changeKeywords(letter) {
      this.setState({ keywords: letter });
    }

    render() {
        return (
            <div style={{
                'backgroundColor' : '#fff'
            }}>
            <title>Catagory</title>
            <div style={{display: this.state.isLoading ? 'block' : 'none'}}>
                <Dimmer active inverted>
                    <Loader size='large'>Model Loading...</Loader>
                </Dimmer>
            </div>
            <Main>
                <div className="container">
                    <div className="row justify-content-center">
                        <div className="col-12 col-lg-8">
                            <SinglePost
                                topics={this.state.topics}
                                open={this.state.open}
                                onOpenModal={this.onOpenModal}
                                onCloseModal={this.onCloseModal}
                                changeKeywords={this.changeKeywords}
                            />
                        </div>
                        <div className="col-12 col-md-8 col-lg-4">
                            <div className="post-sidebar-area">
                                <TopicCloud
                                    keywords={this.state.keywords}
                                />
                                {HotArticle}
                            </div>
                        </div>
                    </div>
                </div>
                <Modal open={this.state.open} onClose={this.onCloseModal} center>
                    <h2>{this.state.title}</h2>
                    <p style={{ 'whiteSpace' : 'pre-line'}}>
                      {this.state.content}
                    </p>
                </Modal>
            </Main>
            </div>
        )}
}
