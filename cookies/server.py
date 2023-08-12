from flask import Flask, request, render_template, redirect, url_for, make_response, send_from_directory
import os
app = Flask(__name__)
USERNAME='admin'
PASSWORD=os.environ.get('PASSWORD')

@app.route('/')
@app.route('/index')
def index():
    user = request.cookies.get('user')
    if user == 'admin':
        return render_template('flag.html')
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/failed_login', methods=['GET'])
def failed_login():
    return render_template('failed_login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('user', 'admin')
        return resp
    else:
        resp = make_response(redirect(url_for('failed_login')))
        resp.set_cookie('user', 'plebian')
        return resp

@app.route('/style.css')
def style():
    return send_from_directory('static', 'style.css')

app.run(host='0.0.0.0', port=8191, debug=True) # TODO: remove debug=True