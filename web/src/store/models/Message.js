import { types } from 'mobx-state-tree';


export const Message = types.model({
  pk: types.maybe(types.string),
  user_id: types.maybe(types.string),
  from_id: types.maybe(types.string),
  date: types.maybe(types.string),
  text: types.maybe(types.string)
});
