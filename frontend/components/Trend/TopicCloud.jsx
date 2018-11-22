import React, {Component} from 'react';
import styled from 'styled-components';
import { TagCloud } from "react-tagcloud";

const options = {
  luminosity: 'light',
  hue: 'blue'
};


const Element = styled.div`
    .tag-cloud-tag {

    }
`;

const customRenderer = (tag, size, color) => (
 <span key={tag.value} style={{color}} className={`tag-${size}`}>{tag.value}</span>
);

const TopicCloud = ({
    keywords
 }) => {

    return (
        <Element className="" style={{height: '800px'}}>
        <div className="widget-content" style={{height: '800px'}}>
            <TagCloud minSize={18}
                      maxSize={42}
                      tags={keywords}
                      colorOptions={options}
                      renderer={customRenderer}
            />
        </div>
        </Element>
    )
}

export default TopicCloud;
