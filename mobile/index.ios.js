/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */

import React, {
  AppRegistry,
  Component,
  StyleSheet,

} from 'react-native';

var LoginPage = require('./LoginPage');

class mobile extends Component{
  render() {
    return (
        <LoginPage />
      );
    }
}



AppRegistry.registerComponent('mobile', () => mobile);
