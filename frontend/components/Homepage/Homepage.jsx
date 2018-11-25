import PropTypes from 'prop-types'
import React, { Component } from 'react'
import {
  Button,
  Container,
  Divider,
  Grid,
  Header,
  Icon,
  Image,
  List,
  Menu,
  Responsive,
  Segment,
  Sidebar,
  Visibility,
} from 'semantic-ui-react'
import bg1 from '../../dist/img/blog-img/bg1.png';
import bg3 from '../../dist/img/blog-img/bg3.png';

const HomepageHeading = ({ mobile }) => (
  <Container text>
      <title>Homepage</title>
    <Header
      as='h1'
      content='Spread the creating !'
      inverted
      style={{
        fontSize: mobile ? '2em' : '4em',
        fontWeight: 'normal',
        marginBottom: 0,
        marginTop: mobile ? '1.5em' : '3em',
      }}
    />
    <Header
      as='h2'
      content='散佈·創作 (ゝ∀･)つ'
      inverted
      style={{
        fontSize: mobile ? '1.5em' : '1.7em',
        fontWeight: 'normal',
        marginTop: mobile ? '0.5em' : '1.5em',
      }}
    />
  </Container>
)

HomepageHeading.propTypes = {
  mobile: PropTypes.bool,
}


class DesktopContainer extends Component {
  state = {}

  hideFixedMenu = () => this.setState({ fixed: false })
  showFixedMenu = () => this.setState({ fixed: true })

  render() {
    const { children } = this.props
    const { fixed } = this.state

    return (
      <Responsive minWidth={Responsive.onlyTablet.minWidth}>
          <Segment
            inverted
            textAlign='center'
            style={{
                minHeight: 600,
                padding: '1em 0em',
                height: '100%',
                overflow: 'hidden',
                background: `url(https://i.imgur.com/fADjmMF.png) no-repeat center center`,
                backgroundSize: 'cover',
                opacity: '0.7'
            }}
            vertical
          >
             <Container>
                 <HomepageHeading />
             </Container>

          </Segment>

        {children}
      </Responsive>
    )
  }
}

DesktopContainer.propTypes = {
  children: PropTypes.node,
}

class MobileContainer extends Component {
  state = {}

  handlePusherClick = () => {
    const { sidebarOpened } = this.state

    if (sidebarOpened) this.setState({ sidebarOpened: false })
  }

  handleToggle = () => this.setState({ sidebarOpened: !this.state.sidebarOpened })

  render() {
    const { children } = this.props
    const { sidebarOpened } = this.state

    return (
      <Responsive maxWidth={Responsive.onlyMobile.maxWidth}>
        <Sidebar.Pushable>
          <Sidebar.Pusher
            dimmed={sidebarOpened}
            onClick={this.handlePusherClick}
            style={{ minHeight: '100vh' }}
          >
            <Segment
              inverted
              textAlign='center'
              style={{ minHeight: 350, padding: '1em 0em', backGround: 'url(http://www.kristianhall.com/wp-content/uploads/2017/06/free-alphabet-clipart-letters-co.jpg)' }}
              vertical
            >
              <HomepageHeading mobile />
            </Segment>
            {children}
          </Sidebar.Pusher>
        </Sidebar.Pushable>
      </Responsive>
    )
  }
}

MobileContainer.propTypes = {
  children: PropTypes.node,
}

const ResponsiveContainer = ({ children }) => (
  <div>
    <DesktopContainer>{children}</DesktopContainer>
    <MobileContainer>{children}</MobileContainer>
  </div>
)

ResponsiveContainer.propTypes = {
  children: PropTypes.node,
}

const HomepageLayout = () => (
  <ResponsiveContainer>
    <Segment style={{ padding: '8em 0em' }} vertical>
      <Grid container stackable verticalAlign='middle' celled='internally'>
        <Grid.Row>
          <Grid.Column width={8}>
            <Header as='h3' style={{ fontSize: '2em' }}>
                主題自動分群
            </Header>
            <p style={{ fontSize: '1.33em' }}>
                經由自動分群後，使文章可以自動進行分類，達成無須人工
           篩選之繁瑣程序
            </p>
            <Header as='h3' style={{ fontSize: '2em' }}>
                支援多種資料來源 ( e.g. 新聞、畫家、個人粉專 )
            </Header>
            <p style={{ fontSize: '1.33em' }}>
                由於資料透過中文自然語言處理，故其亦可適用於其他類型之
          文本分析，諸如新聞、畫家、或是其他中文語言資料集
            </p>
          </Grid.Column>
          <Grid.Column floated='right' width={6}>
            <Image bordered rounded size='large' src={bg1} />
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
    <Segment style={{ padding: '8em 0em' }} vertical>
        <Grid container stackable verticalAlign='middle' celled='internally'>
          <Grid.Row>
            <Grid.Column width={16}>
          <Header as='h3' style={{ fontSize: '2em' }}>
              趨勢變化, 畫家關聯
          </Header>
          <p style={{ fontSize: '1.33em' }}>
             查看訓練後的文字收斂狀況, 觀察彼此的關系
          </p>
        </Grid.Column>
        <Divider
          as='h4'
          className='header'
          horizontal
          style={{ margin: '3em 0em', textTransform: 'uppercase' }}
        >
          <a href='#'>我是分隔線</a>
        </Divider>
        <Grid.Column width={16}>
          <Header as='h3' style={{ fontSize: '2em' }}>
            自定義主題, 客製化調整
          </Header>
          <p style={{ fontSize: '1.33em' }}>
            限定收斂範圍, 讓展覽或是門路不再侷限, 找出有興趣, 或是類似相關的主題吧！
          </p>
          </Grid.Column>
          </Grid.Row>
          </Grid>
      </Segment>
  </ResponsiveContainer>
)
export default HomepageLayout
