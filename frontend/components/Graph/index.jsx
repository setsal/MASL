import React, { Component } from 'react';
import styled from 'styled-components';
import { Container, Header, Segment } from 'semantic-ui-react'
import { Graph } from 'react-d3-graph';
// import { data } from './Static'
const images = require.context('../../dist/img/fb-club-img', true)
const imagePath = (name) => images(name, true)

const myConfig = {
    "automaticRearrangeAfterDropNode": true,
    "collapsible": true,
    "directed": false,
    "height": 800,
    "highlightDegree": 2,
    "highlightOpacity": 0.2,
    "linkHighlightBehavior": true,
    "maxZoom": 12,
    "minZoom": 0.05,
    "focusZoom": 1,
    "focusAnimationDuration": 0.75,
    "nodeHighlightBehavior": true,
    "panAndZoom": false,
    "staticGraph": false,
    "width": 1200,
    "d3": {
      "alphaTarget": 0.05,
      "gravity": -500,
      "linkLength": 150,
      "linkStrength": 2
    },
    "node": {
      "color": "#d3d3d3",
      "fontColor": "black",
      "fontSize": 10,
      "fontWeight": "normal",
      "highlightColor": "red",
      "highlightFontSize": 14,
      "highlightFontWeight": "bold",
      "highlightStrokeColor": "red",
      "highlightStrokeWidth": 1.5,
      "mouseCursor": "crosshair",
      "labelProperty": "name",
      "opacity": 0.9,
      "renderLabel": true,
      "size": 200,
      "strokeColor": "none",
      "strokeWidth": 1.5,
      "svg": "https://cdn.svgporn.com/logos/elasticbox.svg",
      "symbolType": "circle"
    },
    "link": {
      "color": "lightgray",
      "highlightColor": "red",
      "mouseCursor": "pointer",
      "opacity": 1,
      "semanticStrokeWidth": true,
      "strokeWidth": 3,
    }
};

const Main = styled.main`
    padding: 36px 0 47px;
    text-align: center;
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
`;


class AssGraph extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data2: [],
            isLoading: true
        }
    }

    async componentWillMount() {
        const res = await fetch('http://localhost:8000/fb_graph/')
        const data2 = await res.json()
        data2.nodes.map((singledata , index ) => {
            if( typeof singledata.id === 'number' )
                data2.nodes[index]['svg'] = (imagePath('./'+ singledata.id + '.jpg'))

        });
        this.setState({
          data2,
          isLoading: false
        });
    }



    render() {
        if ( this.state.isLoading ) return null;
        if ( !this.state.isLoading )
        return (
            <div style={{
                marginBottom: '50px'
            }}>
                <title>臉書社團關聯</title>

                <Main>
                    <Container>
                        <Header as='h2' textAlign='center' style={{ marginTop: '1.2rem'}}>
                                臉書社團關聯
                        </Header>
                        <Segment>
                            <Graph
                                id="graph-id"
                                data={this.state.data2}
                                config={myConfig}
                            />
                        </Segment>
                    </Container>
                </Main>
            </div>
        )
    }
}

export default AssGraph
