import React, { Component } from 'react'
import styled from 'styled-components'
import {
    Button,
    Checkbox,
    Form,
    Grid,
    Header,
    Segment,
    Container,
    Icon,
} from 'semantic-ui-react'
 import axios from 'axios'

const Main = styled.main`
    text-align: center;
    padding: 15em 0em;
`;

const options = [
  { key: 1, text: '30', value: 30 },
  { key: 2, text: '40', value: 40 },
  { key: 3, text: '50', value: 50 },
  { key: 4, text: '60', value: 60 },
  { key: 5, text: '70', value: 70 },
  { key: 6, text: '80', value: 80 },
]



class Customize extends Component {

    constructor(props) {
        super(props);
        this.state = {
            n_article: '',
            keywords: '',
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        const { name, value } = e.target;
        // console.log(name, value);
        this.setState({ [name]: value });
     }

     handleSelect(e ,data) {
         const { name, value } = data;
         // console.log( name, value );
         this.setState({ [name]: value });
      }

    handleSubmit(e) {
        e.preventDefault();
        const customize = {
          n_article: this.state.n_article,
          keywords: this.state.keywords,
        }

        let uri = 'http://localhost:8000/fb_cluster/customize';


        axios.post(uri, customize)
            .then((response) => {
                let path = {
                    pathname: '/FBcustomize/',
                    state: response.data,
                }
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
                                      </Form.Group>
                                      <Form.TextArea label='關聯字' placeholder='寫下更多..' name="keywords" onChange={this.handleChange} />
                                      <Form.Button>Submit</Form.Button>
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
