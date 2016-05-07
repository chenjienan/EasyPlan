//login page object


import React, {
  Component,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableHighlight,

} from 'react-native';

var Button = require('./3rdParty/Button');
var SignupPage = require('./SignupPage');
class LoginPage extends Component {
  constructor() {
    super();
    this.state={
      username: "",
      password: "",
      page: 0
    };
  }

  onPressButton() {
    this.setState(
      {
      username: '',
      password: '',
      page: 1
      }
    );
  }
  render() {
    switch(this.state.page) {
      case 1:
      return (
        <SignupPage />
      );
      /*case 2:
        return(
          <MainPage />
          );*/
      default:
        return(
          <View style={styles.container}>
          <Text style={styles.title}> Easy Planning </Text>
          <View style={styles.input_view} >
            <Text style={styles.text}> Uid:</Text>
            <TextInput
                style={styles.input}
                onChangeText={(username) => this.setState({username})}
                value={this.state.username} />
            </View>

            <View style={styles.input_view} >
              <Text style={styles.text}> Pwd:</Text>
                <TextInput
                style={styles.input}
                onChangeText={(password) => this.setState({password})}
                value={this.state.password} 
                secureTextEntry = {true} />
            </View>

            <View style = {styles.buttons}>
                    <Button
                      onPress = {this.onPressButton.bind(this)}
                      containerStyle={styles.Signup_button}
                      style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                      Sign up
                    </Button>

                    <Button
                      onPress = {this.onPressButton.bind(this)}
                      containerStyle={styles.Login_button}
                      style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                      Log in
                    </Button>
            </View>
          </View>
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
    width: 200, 
    height: 40, 
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