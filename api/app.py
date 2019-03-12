from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from src import DevelopmentConfig, init_routes, db


app = Flask(__name__)
CORS(app)
api = Api(app)

app.config.from_object(DevelopmentConfig)
db.init_app(app)

init_routes(api)


if __name__ == '__main__':
    app.run()
