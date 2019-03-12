import React from "react";
import { observer } from "mobx-react";
import Button from '@material-ui/core/Button';
import FormControl from '@material-ui/core/FormControl';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import store from "../store/RootStore";
import MessageCard from '../components/MessageCard';


class DialogScreen extends React.Component {
  
  constructor(props) {
    super(props);
    this.user_pk = parseInt(this.props.match.params.user_pk, 10);
    this.sendMessageOnComponent = this.sendMessageOnComponent.bind(this);
    this.state = {
      text: ''
    }
  }

  componentDidMount() {
    store.loadDialogMessages(this.user_pk);
  }

  componentWillUnmount() {
    store.clearMessages();
  }

  sendMessageOnComponent() {
    store.sendMessage(this.user_pk, this.state.text);
    this.state.text = ''
  }

  render() {
    return (
      <div>
        
        <h2>Dialog {this.user_pk}</h2>

        <FormControl variant="outlined">
          <OutlinedInput 
            value={ this.state.text }
            onChange={ evt => this.updateText(evt) }
          />
          <Button 
            variant="contained" 
            color="primary"
            onClick={ this.sendMessageOnComponent }
          >
            Отправить
          </Button>
        </FormControl>
        <div>
          { store.messages.map(message => <MessageCard { ...message }/>) }
        </div>
      </div>
    );
  }

  updateText(evt) {
    this.setState({
      text: evt.target.value
    });
  }
}

export default observer(DialogScreen);
