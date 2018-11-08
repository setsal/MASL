import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import bg1 from '../../dist/img/blog-img/bg1.png';
import Modal from "react-responsive-modal";

const images = require.context('../../dist/img/fb-club-img', true)
const imagePath = (name) => images(name, true)


const contentStyle = {
    'textAlign': 'left',
    whiteSpace: 'pre-line'
}


const SinglePost = ({
        topics,
        open,
        onOpenModal,
        onCloseModal,
        changeKeywords
    }) => {

    const topicTabs = topics.map((topic, index) => {
        return (
            <li className="nav-item" key={index}>
                <a className="nav-link" id="tab2" data-toggle="tab" href={'#world-tab-' + index} role="tab" aria-controls="world-tab-2" aria-selected="false" onClick={() => changeKeywords(topics[index]['keyword_of_topic'])}>{topic.kind}</a>
            </li>
        )
    });

    const articleContents = topics.map((topic, index) => {

        if (index == 0) {
            return (

                <div key={index} className="tab-pane fade show active" id={'world-tab-' + index} role="tabpanel" aria-labelledby={'tab' + index}>
                {
                    topic.articles.map((d, index_inner) => (

                        <div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <div className="post-thumbnail">
                            {

                                <img src={imagePath('./'+ d.clubs_id + '.jpg')} alt=""/>

                            }
                        </div>

                        <div className="post-content">
                            <a href="#" className="headline">
                                <h5>{d.title}</h5>
                            </a>
                            <div style={contentStyle}>
                            {
                                d.content.split("\n").slice(0, 5).map((i, key) => {
                                        return <div key={key}>{i}</div>;
                                })
                            }
                        </div>
                            <a className="btn" onClick={() => onOpenModal(d.content, d.title)}>... read more</a>
                        </div>
                        </div>

                    ))
                }
                </div>

            )
        } else {
            return (
                <div key={index} className="tab-pane fade" id={'world-tab-' + index} role="tabpanel" aria-labelledby={'tab' + index}>
                {
                    topic.articles.map((d, index_inner) => {
                        return (
                            <div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                            <div className="post-thumbnail">
                                <img src={imagePath('./'+ d.clubs_id + '.jpg')} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>{d.title}</h5>
                                </a>
                                <div style={contentStyle}>
                                {
                                    d.content.split("\n").slice(0, 5).map((i, key) => {
                                            return <div key={key}>{i}</div>;
                                    })
                                }
                                </div>
                                <a className="btn" onClick={() => onOpenModal(d.content, d.title)}>...read more</a>
                            </div>
                            </div>
                        )
                    })
                }
                </div>

            )
        }
    });

    return (

        <div className="post-content-area mb-100">
        <div className="world-catagory-area">
            <ul className="nav nav-tabs" id="myTab" role="tablist">
                <li className="title">主題文章</li>
                {topicTabs}
            </ul>

            <div className="tab-content" id="myTabContent">
                {articleContents}
            </div>
        </div>
        </div>
    )
}

export const HotArticle = (<div className="sidebar-widget-area">
    <h5 className="title">數據資料</h5>
    <div className="widget-content">
        <p>目前社團總數: 273 個</p>
        <p>文章總數: 3857 篇</p>
    </div>
</div>)

export default SinglePost;
