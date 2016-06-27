import React, {
  Component,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableHighlight,
  ScrollView,
} from 'react-native';

var Button = require('./3rdParty/Button');
var LoginPage = require('./LoginPage');

//Sign up page
class SignupPage extends Component {
  constructor() {
    super();
    this.state = {
      firstName: '',
      lastName: '',
      pwd: '',
      confirmPwd: '',
      email: ''
    };
  }

   

	render() {
		  return(
        <View style={styles.container}>
          <ScrollView 
          ref='scrollView' 
          keyboardDismissMode='interactive' 
          style={styles.scrollView} 
          contentContainerStyle={styles.contentContainerStyle}>
		    		<Text style = {styles.title}>  Sign Up </Text>
            <InputView value={this.state.email}
             onChangeText={(email)=>this.setState({email})}
               inputStyle={styles.input}
              textStyle={styles.text}>
              Email:
            </InputView>
           <InputView value={this.state.pwd}
              onChangeText={(pwd)=>this.setState({pwd})}
              inputStyle={styles.input}
              textStyle={styles.text}
            secureTextEntry={true}>
            Password:
          </InputView>

          <InputView value={this.state.confirmPwd}
            onChangeText={(confirmPwd)=>this.setState({confirmPwd})}
            inputStyle={styles.input}
            textStyle={styles.text}
            secureTextEntry={true}>
            Confirm Password:
          </InputView>

          <InputView value={this.state.firstName}
            onChangeText={(firstName)=>this.setState({firstName})}
            inputStyle={styles.input}
            textStyle={styles.text}>
            First Name:
          </InputView>

          <InputView value={this.state.lastName}
            onChangeText={(lastName)=>this.setState({lastName})}
            inputStyle={styles.input}
            textStyle={styles.text}>
            Last Name:
          </InputView>
          <View style = {styles.buttons}>
                <Button
                  onPress = {this.onPressSignUpButton.bind(this)}
                  containerStyle={styles.SignUp_button}
                  style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                  Sign up
                </Button>

                <Button
                  onPress = {this.onPressCancelButton.bind(this)}
                  containerStyle={styles.Cancel_button}
                  style={{margin:8,fontSize: 15,alignItems: 'center', color: 'white'}}>
                  Cancel
                </Button>
            </View>
          </ScrollView>
        </View>
		);
	}
  onPressSignUpButton() {
    console.log(this.props);
    this.props.callBack(0);
  }
  onPressCancelButton() {
    this.props.callBack(0);
  }
}

class InputView extends Component {
  render() {
    var inputproperties = {
      onChangeText: this.props.onChangeText,
      value: this.props.value,
      style: this.props.inputStyle,
      secureTextEntry: this.props.secureTextEntry,
    };
    return (
      <View style={styles.inputView}>
        <Text style={this.props.textStyle}>{this.props.children}</Text>
        <TextInput {...inputproperties} />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  scrollView: {
    height: 300,
    width: 250
  },
  contentContainerStyle: {
    flex: 0,
  },
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

  input: {
    width: 250, 
    height: 25, 
    marginTop: 20,
    backgroundColor: 'white', 
    borderWidth: 0,
  },
  input_view: {
    flexDirection: 'row',
    width: 250, 
    height: 40, 
    marginTop: 20,
  },
  text: {
    paddingTop: 10,
    textAlign: 'left',
    fontSize: 15,
    color: 'white',
  },
  SignUp_button: {
    marginTop:20, 
    height:35, 
    overflow:'hidden', 
    alignItems: 'flex-start',
    borderRadius:4, 
    backgroundColor: 'green',
  },
  Cancel_button: {
    marginTop:20, 
    height:35, 
    overflow:'hidden', 
    alignItems: 'flex-end', 
    borderRadius:4, 
    backgroundColor: 'red',
  },
});

module.exports = [SignupPage,InputView]