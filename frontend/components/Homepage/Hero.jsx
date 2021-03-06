import React, {Component} from 'react';
import '../../dist/hero.css';
import styled from 'styled-components';
import bg1 from '../../dist/img/blog-img/bg1.png';
import bg2 from '../../dist/img/blog-img/bg2.jpg';
import bg3 from '../../dist/img/blog-img/bg3.jpg';
import Slider from "react-slick";

const BGIMG = styled.div`
    background-image: url(${bg1})
`
const BGIMG2 = styled.div`
    background-image: url(${bg2})
`

const BGIMG3 = styled.div`
    background-image: url(${bg3})
`

export default class Hero extends Component {
    render() {
        var settings = {
          dots: false,
          infinite: true,
          autoplaySpeed: 6000,
          slidesToShow: 1,
          autoplay: true,
          arrows: false,
        };
        return (
            <div className="hero-area">
                <div className="hero-slides">
                    <Slider {...settings}>
                        <BGIMG3 className="single-hero-slide bg-img background-overlay" >
                            <div>hihi2</div>
                        </BGIMG3>
                        <BGIMG className="single-hero-slide bg-img background-overlay" >
<div style={{'color': '#fff'}}>hihi23</div>
                        </BGIMG>
                        <BGIMG2 className="single-hero-slide bg-img background-overlay" >
<div>hihi2</div>
                        </BGIMG2>
                        
                    </Slider>
                </div>
            </div>

        )
    }
}
