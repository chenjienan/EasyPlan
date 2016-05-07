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
	render() {
		return(
			<View style={styles.container}>
				<Text style = {styles.title}>  I am signUp page </Text>
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

  inputs: {
    width: 250, 
    height: 40, 
    marginTop: 20,
    backgroundColor: 'white', 
    borderWidth: 0,
  },
  text: {
    textAlign: 'center',

  }
});

module.exports = SignupPage;