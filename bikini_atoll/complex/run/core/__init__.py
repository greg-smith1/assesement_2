#!/usr/bin/env python3

import os
import sqlite3
from flask import Flask, render_template, request, url_for, redirect

#import core.controllers.login
from core.controllers.general import controller as general
from core.controllers.bicycle import controller as bicycle


def keymaker(omnibus, filename='secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    print('Pathname:', pathname)
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {0}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {0}'.format(pathname))
        omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()


omnibus = Flask(__name__)

def users():
    log = []
    connection = sqlite3.connect('../run/datastore/master.db', check_same_thread = False)
    cursor     = connection.cursor()
    cursor.execute("""SELECT username FROM users;""")
    username = cursor.fetchone()[0]
    log.append(username)
    cursor.execute("""SELECT password FROM users;""")
    password = cursor.fetchone()[0]
    log.append(password)
    return log

@omnibus.route('/login/', methods=['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        print('GET!!!')
        return render_template('login.html')
    else:
        log = users()
        print(log)
        username = request.form['username']
        password = request.form['password']
        if username == log[0]:
            if password == log[1]:
                return redirect('/')
        else:
            return render_template('login.html', message='Error: Bad Credentials')

#omnibus.register_blueprint(login)
omnibus.register_blueprint(general)
omnibus.register_blueprint(bicycle)

keymaker(omnibus)

