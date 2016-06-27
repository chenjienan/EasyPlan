//login page object


import React, {
  Component,
  StyleSheet,
  Text,
  View,
  ScollView,
  TextInput,
  TouchableHighlight,

} from 'react-native';

var Button = require('./3rdParty/Button');
var [SignupPage, Inputview] = require('./SignupPage');
class LoginPage extends Component {
  constructor() {
    super();
    this.state={
      username: "",
      password: "",
      page: 0
    };
  }

  onPressSignUpButton() {
    this.setState(
      {
      username: '',
      password: '',
      page: 1
      }
    );
  }
  changeState0(page_num) {
    this.setState({
      username: "",
      password: "",
      page: page_num
    });
  }
  onPressLoginButton() {
    fetch('http://172.16.21.55:5000/login', {
      method: 'POST',
      headers: {
       'Accept': 'application/json',
       'Content-Type' : 'application/json'
     },
     body: JSON.stringify({
        'username': this.state.username,
        'password': this.state.password
     })
    }).then((response)=>response.text()).then((responseText)=>{
      console.log("request success with response",responseText);
    }).catch((error)=>{
      
      console.log(error);
      
    });
  }
  render() {
    switch(this.state.page) {
      case 1:
      return (
        <SignupPage callBack={this.changeState0.bind(this)} />
      );
      /*case 2:
        return(
          <MainPage />
          );*/
      default:
        return(
            <View style={styles.container}>
            <Text style={styles.title}> Easy Planning </Text>
              <Inputview
                 onChangeText={(username) => this.setState({username})}
                 value={this.state.username}
                 inputStyle={styles.input}
                 textStyle = {styles.text} >
                User Name:
              </Inputview>

              <Inputview
                inputStyle={styles.input}
                textStyle = {styles.text}
                onChangeText={(password) => this.setState({password})}
                value={this.state.password} 
                secureTextEntry = {true}>
                Password:
              </Inputview>

             <View style = {styles.buttons}>
                      <Button
                        onPress = {this.onPressSignUpButton.bind(this)}
                        containerStyle={styles.Signup_button}
                        style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                        Sign up
                     </Button>

                      <Button
                       onPress = {this.onPressLoginButton.bind(this)}
                        containerStyle={styles.Login_button}
                        style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                        Log in
                      </Button>
              </View>
            </View>
          //</ScollView>
        );
      }
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: 'gray',
  },
  buttons: {
    flexDirection: 'row',
  },
  title: {
    fontSize: 25,
    textAlign: 'center',
    paddingTop: 100,
    color: 'white',
  },
  text: {
    paddingTop: 10,
    textAlign: 'left',
    fontSize: 15,
    color: 'white',
  },
  input_view: {
    flexDirection: 'row',
    width: 250, 
    height: 40, 
    marginTop: 20,
  },
  input: {
    width: 250, 
    height: 25, 
    backgroundColor: 'white', 
    borderWidth: 0,
  },
  Signup_button: {
    marginTop:20, 
    height:35, 
    overflow:'hidden', 
    alignItems: 'flex-start',
    borderRadius:4, 
    backgroundColor: 'blue',
  },
  Login_button: {
    marginTop:20, 
    height:35, 
    overflow:'hidden', 
    alignItems: 'flex-end', 
    borderRadius:4, 
    backgroundColor: 'green',
  },
});

module.exports = LoginPage;