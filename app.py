from flask import Flask, jsonify
from views import api


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(api)


if __name__ == '__main__':
    app.run()
