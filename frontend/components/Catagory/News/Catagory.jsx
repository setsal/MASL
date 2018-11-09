import React, {Component} from 'react';
import styled from 'styled-components';
import '../../../dist/catagory.css';
const images = require.context('../../../dist/img/media-img', true)
const imagePath = (name) => images(name, true)

const contentStyle = {
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
                    topic.articles.map((d, index_inner) => (<div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <div className="post-thumbnail">
                            {

                                <img src={imagePath('./'+ d.company_id + '.png')} alt=""/>

                            }
                        </div>
                        <div className="post-content">
                            <a className="headline btn" onClick={() => onOpenModal(d.content, d.title)} >
                                <h5>{d.title}</h5>
                            </a>
                            <div className="post-meta">
                                <p>
                                    <a href="#" className="post-author">{d.company}&nbsp;</a>
                                    -
                                    <a href="#" className="post-date">&nbsp;{d.category}</a>
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
                            {

                                <img src={imagePath('./'+ d.company_id + '.png')} alt=""/>

                            }
                        </div>

                        <div className="post-content">
                            <a className="headline btn" onClick={() => onOpenModal(d.content, d.title)} >
                                <h5>{d.title}</h5>
                            </a>
                            <div className="post-meta">
                                <p>
                                    <a href="#" className="post-author">{d.company}&nbsp;</a>
                                    -
                                    <a href="#" className="post-date">&nbsp;{d.category}</a>
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
                <li className="title">主題文章</li>
                {topicTabs}
            </ul>

            <div className="tab-content" id="myTabContent">
                {articleContents}
            </div>
        </div>
    </div>)
}

export const HotArticle = (<div className="sidebar-widget-area">
    <h5 className="title">Hot Article</h5>
    <div className="widget-content">
        <p>目前新聞來源: 4 間</p>
        <p>文章總數: 1517 篇</p>
    </div>
</div>)

export default SinglePost;
