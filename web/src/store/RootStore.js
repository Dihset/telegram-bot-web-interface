import axios from 'axios';
import { types, flow } from 'mobx-state-tree';
import { DIALOGS_URL } from '../utils/constants';
import { Dialog } from './models/Dialog';
import { Message } from './models/Message'


const RootStore = types
  .model({
    dialogs: types.maybe(types.array(Dialog)),
    messages: types.maybe(types.array(Message))
  })
  .actions(self => ({

    loadDialogList: flow(function*() {
      const { data } = yield axios.get(DIALOGS_URL);
      self.dialogs = data;
    }),

    loadDialogMessages: flow(function*(user_pk) {
      const { data } = yield axios.get(`${DIALOGS_URL}${user_pk}/`);
      self.messages = data;
      self.messages = self.messages.sort((a, b) => -(parseInt(a.pk)-parseInt(b.pk)));
    }),

    clearMessages: function() {
      self.messages = [];
    },

    sendMessage: flow(function*(user_pk, text) {
      yield axios.post(
        `${DIALOGS_URL}${user_pk}/`, 
        {
          'text': text
        }
      )
      self.loadDialogMessages(user_pk);
    })
      

  }))
  .create({
    dialogs: [],
    messages: []
  });

export default RootStore;
