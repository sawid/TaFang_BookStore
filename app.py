from flask import Flask, render_template, jsonify, request, redirect, url_for
from routes import route
from database import DB
from name import Name

app = Flask(__name__)

DB.init()

app.register_blueprint(route.get_blueprint())

if __name__ == '__main__':
    app.run(debug=True)