import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import bg1 from '../../dist/img/blog-img/bg1.png';

class SinglePost extends Component {

    render() {
        return (<div className="post-content-area mb-100">
            <div className="world-catagory-area">
                <ul className="nav nav-tabs" id="myTab" role="tablist">
                    <li className="title">Don't Miss</li>

                    {
                        this.props.KindList.map(function(kind, index) {
                            return (<li className="nav-item" key={index}>
                                <a className="nav-link" id="tab2" data-toggle="tab" href={'#world-tab-' + index } role="tab" aria-controls="world-tab-2" aria-selected="false">{kind.name}</a>
                            </li>)
                        })
                    }
                </ul>

                <div className="tab-content" id="myTabContent">

                    <div className="tab-pane fade show active" id="world-tab-0" role="tabpanel" aria-labelledby="tab0">

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist1</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist2</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                    </div>

                    <div className="tab-pane fade" id="world-tab-1" role="tabpanel" aria-labelledby="tab1">

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist3</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist4</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="tab-pane fade" id="world-tab-3" role="tabpanel" aria-labelledby="tab3">

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist5</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist6</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="tab-pane fade" id="world-tab-4" role="tabpanel" aria-labelledby="tab4">

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist7</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist8</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="tab-pane fade" id="world-tab-5" role="tabpanel" aria-labelledby="tab5">

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="single-blog-post post-style-4 d-flex align-items-center">

                            <div className="post-thumbnail">
                                <img src={bg1} alt=""/>
                            </div>

                            <div className="post-content">
                                <a href="#" className="headline">
                                    <h5>Title</h5>
                                </a>
                                <p>Content</p>

                                <div className="post-meta">
                                    <p>
                                        <a href="#" className="post-author">Artist</a>
                                        on
                                        <a href="#" className="post-date">Timestamp</a>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>)
    }
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
                    <h5 className="mb-0">血小板好像太多惹</h5>
                </a>
            </div>
        </div>

        <div className="single-blog-post post-style-2 d-flex align-items-center widget-post">

            <div className="post-thumbnail">
                <img src={bg1} alt=""/>
            </div>

            <div className="post-content">
                <a href="#" className="headline">
                    <h5 className="mb-0">血小板好像太多惹</h5>
                </a>
            </div>
        </div>

    </div>
</div>)

export default SinglePost;
