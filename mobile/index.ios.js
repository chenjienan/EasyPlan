/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */

import React, {
  AppRegistry,
  Component,
  StyleSheet,
  Text,
  View,
  Navigator,
  TextInput,
  TouchableHighlight,

} from 'react-native';

class mobile extends Component {
  constructor() {
    super();
    this.state={
      username: "",
      password: ""
    };
  }
  render() {
    return (
      <View style={styles.container}>
        <Text style= {styles.title}> Easy Planning </Text>
        <View stype={styles.inputs}>
          <TextInput
                style={styles.inputs}
                onChangeText={(username) => this.setState({username})}
                value={this.state.username} />

                <TextInput
                style={styles.inputs}
                onChangeText={(password) => this.setState({password})}
                value={this.state.password} 
                secureTextEntry = {true} />

                <TouchableHighlight
                  onPress = {this._onPressButton}
                  style={styles.button}>
                  <Text style= {styles.text}>
                  Clear me!
                  </Text>
                </TouchableHighlight>
        </View>
      </View>
    );
  }

  _onPressButton() {
    console.log(this);
    console.log(this.state);
    this.state.username="";
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: 'gray',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
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
  button: {

    width: 200,
    alignItems: 'center', 
    paddingTop: 10,
    height: 40,
  },
  text: {
    textAlign: 'center',

  }
});

AppRegistry.registerComponent('mobile', () => mobile);
