import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import bg1 from '../../dist/img/blog-img/bg1.png';


const SinglePost = (<div className="post-content-area mb-100">
    <div className="world-catagory-area">
        <ul className="nav nav-tabs" id="myTab" role="tablist">
            <li className="title">Don't Miss</li>

            <li className="nav-item">
                <a className="nav-link active" id="tab1" data-toggle="tab" href="#world-tab-1" role="tab" aria-controls="world-tab-1" aria-selected="true">All</a>
            </li>

            <li className="nav-item">
                <a className="nav-link" id="tab2" data-toggle="tab" href="#world-tab-2" role="tab" aria-controls="world-tab-2" aria-selected="false">Kind</a>
            </li>

            <li className="nav-item">
                <a className="nav-link" id="tab3" data-toggle="tab" href="#world-tab-3" role="tab" aria-controls="world-tab-3" aria-selected="false">Kind</a>
            </li>

            <li className="nav-item">
                <a className="nav-link" id="tab4" data-toggle="tab" href="#world-tab-4" role="tab" aria-controls="world-tab-4" aria-selected="false">Kind</a>
            </li>

            <li className="nav-item">
                <a className="nav-link" id="tab5" data-toggle="tab" href="#world-tab-5" role="tab" aria-controls="world-tab-5" aria-selected="false">Kind</a>
            </li>
        </ul>

        <div className="tab-content" id="myTabContent">

            <div className="tab-pane fade show active" id="world-tab-1" role="tabpanel" aria-labelledby="tab1">

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

            <div className="tab-pane fade" id="world-tab-2" role="tabpanel" aria-labelledby="tab2">

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


export const About = (
        <div className="sidebar-widget-area">
            <h5 className="title">About MASL</h5>
            <div className="widget-content">
                <p>Cheers OAO/</p>
            </div>
        </div>
)

export const HotArticle = (
    <div className="sidebar-widget-area">
        <h5 className="title">Hot Article</h5>
        <div className="widget-content">

            <div className="single-blog-post post-style-2 d-flex align-items-center widget-post">

                <div className="post-thumbnail">
                    <img src={bg1} alt="" />
                </div>

                <div className="post-content">
                    <a href="#" className="headline">
                        <h5 className="mb-0">血小板好像太多惹</h5>
                    </a>
                </div>
            </div>

            <div className="single-blog-post post-style-2 d-flex align-items-center widget-post">

                <div className="post-thumbnail">
                    <img src={bg1} alt="" />
                </div>

                <div className="post-content">
                    <a href="#" className="headline">
                        <h5 className="mb-0">血小板好像太多惹</h5>
                    </a>
                </div>
            </div>

        </div>
    </div>
)

export default SinglePost;
