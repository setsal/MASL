import React, {Component} from 'react';
import styled from 'styled-components';
import '../../dist/catagory.css';
import { TagCloud } from "react-tagcloud";
const options = {
  luminosity: 'light',
  hue: 'blue'
};


const TopicCloud = ({
    keywords
 }) => {

    return (
        <div className="sidebar-widget-area">
        <h5 className="title">構成 Topic 組成</h5>
        <div className="widget-content">
            <TagCloud minSize={18}
                      maxSize={42}
                      tags={keywords}
                      colorOptions={options}
            />
        </div>
        </div>
    )
}

export default TopicCloud;
