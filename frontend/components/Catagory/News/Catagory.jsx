import React, {Component} from 'react';
import styled from 'styled-components';
import '../../../dist/catagory.css';
const images = require.context('../../../dist/img/media-img', true)
const imagePath = (name) => images(name, true)
import { Image, Item } from 'semantic-ui-react'

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
                    topic.articles.map((d, index_inner) => (
                        <div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <Item.Group divided unstackable>
                            <Item>
                              <Item.Image src={imagePath('./'+ d.company_id + '.png')} />

                              <Item.Content style={{ lineHeight: '4' }}>
                                <Item.Header as='a' onClick={() => onOpenModal(d.content, d.title)}>{d.title}</Item.Header>
                                <Item.Meta>{d.company} - {d.category} - {d.timestamp} </Item.Meta>
                                <Item.Description>
                                  <Image src='https://react.semantic-ui.com/images/wireframe/short-paragraph.png' />
                                </Item.Description>
                                <Item.Extra>[相似度]: {d.similarities}</Item.Extra>
                              </Item.Content>
                            </Item>
                        </Item.Group>
                        </div>
                    ))
                }
            </div>)
        } else {
            return (<div key={index} className="tab-pane fade" id={'world-tab-' + index} role="tabpanel" aria-labelledby={'tab' + index}>
                {
                    topic.articles.map((d, index_inner) => (
                        <div key={index_inner} className="single-blog-post post-style-4 d-flex align-items-center">
                        <Item.Group divided unstackable>
                            <Item>
                              <Item.Image src={imagePath('./'+ d.company_id + '.png')} />

                              <Item.Content style={{ lineHeight: '4' }}>
                                <Item.Header as='a' onClick={() => onOpenModal(d.content, d.title)}>{d.title}</Item.Header>
                                <Item.Meta>{d.company} - {d.category} - {d.timestamp} </Item.Meta>
                                <Item.Description>
                                  <Image src='https://react.semantic-ui.com/images/wireframe/short-paragraph.png' />
                                </Item.Description>
                                <Item.Extra>[相似度]: {d.similarities}</Item.Extra>
                              </Item.Content>
                            </Item>
                        </Item.Group>
                        </div>
                    ))
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
        <p>文章總數: 19153 篇</p>
    </div>
</div>)

export default SinglePost;
