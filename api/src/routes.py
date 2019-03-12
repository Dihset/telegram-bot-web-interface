from .views import TelegramHookView, DialogListView, DialogView


def init_routes(api):
    api.add_resource(TelegramHookView, '/639381913:AAF2kHmbSvIGGDOJNj1-1alwuJRhEsijeMU')
    api.add_resource(DialogListView, '/api/dialogs/')
    api.add_resource(DialogView, '/api/dialogs/<int:user_id>/')
