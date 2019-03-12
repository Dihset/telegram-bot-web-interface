import { types } from 'mobx-state-tree';


export const Dialog = types.model({
  pk: types.maybe(types.string),
  username: types.maybe(types.string),
  first_name: types.maybe(types.string),
  last_name: types.maybe(types.string),
  language_code: types.maybe(types.string)
});
