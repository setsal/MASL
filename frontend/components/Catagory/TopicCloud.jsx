import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import { TagCloud } from "react-tagcloud";

const TopicCloud = ({
    keywords
 }) => {
    
    return (
        <div className="sidebar-widget-area">
        <h5 className="title">構成 Topic 組成</h5>
        <div className="widget-content">
            <TagCloud minSize={12}
                      maxSize={35}
                      tags={keywords}
                      onClick={tag => alert(`'${tag.value}' was selected!`)}
            />
        </div>
        </div>
    )
}

export default TopicCloud;
