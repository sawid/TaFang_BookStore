from flask import Blueprint , render_template , request
from name import Name

route = Blueprint('route', __name__)
def get_blueprint():
    """Return the blueprint for the main app module"""
    return route

@route.route('/')
def home():
    return  render_template('home.html')

@route.route('/search')
def search_page():
    return  render_template('search_page.html')

@route.route('/book_detail')
def book_detail():
    return  render_template('book_detail.html')

@route.route('/payment')
def payment():
    return  render_template('payment.html')

@route.route('/addName',methods=['POST'])
def addName():
    username = request.form.get('username','')
    password = request.form.get('password','')
    newName = Name(name=username, password=password)
    newName.insert()
    return ('Success',200)