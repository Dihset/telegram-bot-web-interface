import React from "react";
import { observer } from "mobx-react";
import DialogCard from '../components/DialogCard'
import store from "../store/RootStore";


class DialogListScreen extends React.Component {
  
  componentDidMount() {
    store.loadDialogList();
  }
  
  render() {
    return (
      <div>
        { store.dialogs.map(dialog => <DialogCard { ...dialog }/>) }
      </div>
    )
  }
}

export default observer(DialogListScreen);
