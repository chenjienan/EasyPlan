import React, {
  Component,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableHighlight,
} from 'react-native';


//Sign up page
class SignupPage extends Component {
  constructor() {
    super();
    this.state = {
      firstName: '',
      lastName: '',
      pwd: '',
      email:''
    };
  }
	render() {
		return(
			<View style={styles.container}>
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
      </View>
		);
	}
}

class InputView extends Component {
  render() {
    var inputproperties = {
      onChangeText: this.props.onChangeText,
      value: this.props.value,
      style: this.props.inputStyle,
      secureTextEntry: this.props.secureTextEntry
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
    height: 40, 
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
});

module.exports = [SignupPage,InputView]