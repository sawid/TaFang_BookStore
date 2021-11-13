from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/search')
def search_page():
    return  render_template('search_page.html')

@app.route('/book_detail')
def book_detail():
    return  render_template('book_detail.html')

@app.route('/payment')
def payment():
    return  render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)