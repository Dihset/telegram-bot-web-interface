import React from "react";
import { BrowserRouter as Router, Route, Link} from "react-router-dom";
import { observer } from 'mobx-react'
import DialogListScreen from "../screens/DialogListScreen";
import DialogScreen from "../screens/DialogScreen";

const routeEntry = observer(props => 
  <Router>
    <div>
      <Route exact path='/' component={ DialogListScreen }/>
      <Route path='/dialog/:user_pk' component={ DialogScreen }/>
    </div>
  </Router>
  )
    
export default routeEntry;