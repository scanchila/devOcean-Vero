import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Landing from '../containers/Landing';
import Login from '../containers/Login';

const App = () => (
  <Router>
    <Switch>
      <Route exact path='/'>
        <Landing />
      </Route>
      <Route exact path='/login'>
        <Login />
      </Route>
    </Switch>
  </Router>
);

export default App;
