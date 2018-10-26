import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import bg1 from '../../dist/img/blog-img/bg1.png';

const SinglePost = ({topics}) => {
    
    const topicTabs = topics.map((topic, index) => {
        return (<li className="nav-item" key={index}>
            <a className="nav-link" id="tab2" data-toggle="tab" href={'#world-tab-' + index} role="tab" aria-controls="world-tab-2" aria-selected="false">{topic.kind}</a>
        </li>)
    });

    const articleContents = topics.map((topic, index) => {
        if (index == 0) {
            return (<div key={index} className="tab-pane fade show active" id={'world-tab-' + index} role="tabpanel" aria-labelledby={'tab' + index}>
                {
                    topic.articles.map((d, index_inner) => (<div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <div className="post-thumbnail">
                            <img src={bg1} alt=""/>
                        </div>

                        <div className="post-content">
                            <a href="#" className="headline">
                                <h5>{d.title}</h5>
                            </a>
                            <p>{d.content}</p>

                            <div className="post-meta">
                                <p>
                                    <a href="#" className="post-author">Artist1</a>
                                    on
                                    <a href="#" className="post-date">Timestamp</a>
                                </p>
                            </div>
                        </div>
                    </div>))
                }
            </div>)
        } else {
            return (<div key={index} className="tab-pane fade" id={'world-tab-' + index} role="tabpanel" aria-labelledby={'tab' + index}>
                {
                    topic.articles.map((d, index_inner) => (<div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <div className="post-thumbnail">
                            <img src={bg1} alt=""/>
                        </div>

                        <div className="post-content">
                            <a href="#" className="headline">
                                <h5>{d.title}</h5>
                            </a>
                            <p>{d.content}</p>

                            <div className="post-meta">
                                <p>
                                    <a href="#" className="post-author">Artist1</a>
                                    on
                                    <a href="#" className="post-date">Timestamp</a>
                                </p>
                            </div>
                        </div>
                    </div>))
                }
            </div>)
        }
    });

    return (<div className="post-content-area mb-100">
        <div className="world-catagory-area">
            <ul className="nav nav-tabs" id="myTab" role="tablist">
                <li className="title">Don't Miss</li>
                {topicTabs}
            </ul>

            <div className="tab-content" id="myTabContent">
                {articleContents}
            </div>
        </div>
    </div>)
}



export const About = (<div className="sidebar-widget-area">
    <h5 className="title">About MASL</h5>
    <div className="widget-content">
        <p>Cheers OAO/</p>
    </div>
</div>)

export const HotArticle = (<div className="sidebar-widget-area">
    <h5 className="title">Hot Article</h5>
    <div className="widget-content">

        <div className="single-blog-post post-style-2 d-flex align-items-center widget-post">

            <div className="post-thumbnail">
                <img src={bg1} alt=""/>
            </div>

            <div className="post-content">
                <a href="#" className="headline">
                    <h5 className="mb-0">To be continue..</h5>
                </a>
            </div>
        </div>

        <div className="single-blog-post post-style-2 d-flex align-items-center widget-post">

            <div className="post-thumbnail">
                <img src={bg1} alt=""/>
            </div>

            <div className="post-content">
                <a href="#" className="headline">
                    <h5 className="mb-0">To be continue..</h5>
                </a>
            </div>
        </div>

    </div>
</div>)

export default SinglePost;
