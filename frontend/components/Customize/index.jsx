import React, { Component } from 'react'
import styled from 'styled-components'
import {
    Button,
    Checkbox,
    Form,
    Grid,
    Header,
    Segment,
    Dimmer,
    Loader,
    Container,
    Icon,
} from 'semantic-ui-react'
 import axios from 'axios'

const Main = styled.main`
    text-align: center;
    padding: 15em 0em;
`;

const options = [
  { key: 1, text: '10', value: 10 },
  { key: 2, text: '20', value: 20 },
  { key: 3, text: '30', value: 30 },
  { key: 4, text: '40', value: 40 },
  { key: 5, text: '50', value: 50 },
  { key: 6, text: '60', value: 60 },
  { key: 7, text: '70', value: 70 },
  { key: 8, text: '80', value: 80 },
]


const topic_options = [
  { key: 1, text: '5', value: 5 },
  { key: 2, text: '6', value: 6 },
  { key: 3, text: '7', value: 7 },
  { key: 4, text: '8', value: 8 },
  { key: 5, text: '9', value: 9 },
  { key: 6, text: '10', value: 10 },
]


class Customize extends Component {

    constructor(props) {
        super(props);
        this.state = {
            n_article: '',
            n_topic: '',
            keywords: '',
            exhibition: '',
            isloading: false,
            isEnabled: false,
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleCheckBox = this.handleCheckBox.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        const { name, value } = e.target;
        console.log(name, value);
        this.setState({ [name]: value });
     }

     handleCheckBox(e) {
         this.setState({
             isEnabled: true
         });
      }

     handleSelect(e ,data) {
         const { name, value } = data;
         // console.log( name, value );
         this.setState({ [name]: value });
      }

    handleSubmit(e) {
        e.preventDefault();
         this.setState({
             isLoading: true
         });
        const customize = {
          n_article: this.state.n_article,
          n_topic: this.state.n_topic,
          exhibition: this.state.exhibition,
          keywords: this.state.keywords,
        }
        console.log(customize)

        let uri = 'http://localhost:8000/fb_cluster/customize';


        axios.post(uri, customize)
            .then((response) => {
                let path = {
                    pathname: '/fb_result/',
                    state: response.data,
                }
                this.setState({
                    isLoading: false
                });
                this.props.history.push(path);
        })
        .catch(function (error) {
          console.log(error.response.data);
        });
    }

    render() {
        const { value } = this.state

        return (
            <div>
            <title>Customize</title>
                <Main>
                    <div style={{display: this.state.isLoading ? 'block' : 'none'}}>
                        <Dimmer active inverted>
                            <Loader size='large'>Model Building...</Loader>
                        </Dimmer>
                    </div>
                    <Grid container verticalAlign='middle' celled='internally'>
                      <Grid.Row>
                        <Grid.Column width={6}>
                            <Header as='h2' icon textAlign='center'>
                          <Icon name='paper plane outline' />
                          Customize
                          <Header.Subheader>
                            自己決定想看那些東西!
                          </Header.Subheader>
                        </Header>
                        </Grid.Column>
                        <Grid.Column width={10}>
                            <Container>
                            <Form onSubmit={this.handleSubmit}>
                                <Segment stacked>
                                      <Form.Group widths='equal' inline>
                                        <Form.Select fluid label='分類文章數目' name="n_article" options={options} placeholder='數量' onChange={this.handleSelect} />
                                        <Form.Select fluid label='主題數量' name="n_topic" options={topic_options} placeholder='數量' onChange={this.handleSelect} />
                                      </Form.Group>
                                      <Form.TextArea label='關聯字(請以空白分隔) e.g. FGO 少女前線 cosplay' placeholder='寫下更多..' name="keywords" onChange={this.handleChange} />
                                      <Form.Group inline>
                                        <label>選擇展覽區間</label>
                                        <Form.Field label='FF32' control='input' type='radio' name='exhibition' value='FF32' onChange={this.handleChange}/>
                                        <Form.Field label='FF31' control='input' type='radio' name='exhibition' value='FF31' onChange={this.handleChange}/>
                                        <Form.Field label='FF30' control='input' type='radio' name='exhibition' value='FF30' onChange={this.handleChange}/>
                                      </Form.Group>
                                      <Form.Group inline style={{ textAlign: 'left'}}>
      <Form.Checkbox label='我已知悉並了解結果皆為訓練出來的成果，無論好與壞，不可怪罪很辛苦的開發者QAQ' name="checkbox" onClick={this.handleCheckBox} />
      </Form.Group>
                                      <Form.Button disabled={!this.state.isEnabled}>Submit</Form.Button>
                                </Segment>
                            </Form>
                            </Container>
                        </Grid.Column>
                      </Grid.Row>
                    </Grid>
                </Main>
            </div>
        )
    }
}

export default Customize;
