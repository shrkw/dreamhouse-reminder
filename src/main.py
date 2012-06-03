#!/usr/bin/env python
# coding:utf-8

import sys
sys.path.insert(0, "./libs")
sys.path.insert(0, './distlib.zip')

from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask, render_template, request, redirect, flash, url_for

DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

class MailRegisterationForm(object):
    addr = None
    def __init__(self, addr):
        self.addr = addr

    def validate(self):
        ''' TODO '''
        if self.addr == "foo@example.com":
            return True
        else:
            return False

@app.route('/register_address', methods=['POST'])
def register_address():
    form = MailRegisterationForm(request.form.get('email_address'))
    if form.validate():
        send_confirmation_mail(form.addr)
        return redirect(url_for('complete_mail_send'))
    else:
        error = u'メールアドレスが不正と判定されました'
        return render_template('index.html', error=error, addr=form.addr)

@app.route('/complete_mail_send')
def complete_mail_send():
    return render_template('mail_send_complete.html')

def send_confirmation_mail(addr):
    pass

class MailConfirmationForm(object):
    token = None
    def __init__(self, token):
        self.token = token

    def validate(self):
        ''' TODO '''
        pass

@app.route('/confirm_address', methods=['GET'])
def confirm_address():
    form = MailConfirmationForm(request.args.get("token"))
    if form.validate():
        save_validated_address(form.token)

def save_validated_address(token):
    pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    pass

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    pass

@app.route('/flash/<hoge>', methods=['GET'])
def get_flash(hoge):
#    flash('Your flash message is: ')
    flash('Your flash message is: ' + hoge)
#    return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were sucessfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    run_wsgi_app(app)
#    app.run(host='localhost')
