#!/usr/bin/env python3

from flask import Blueprint, render_template, request
import sqlite3

#controller = Blueprint('login', __name__, url_prefix='/login')

def users():
    log = []
    #connection = sqlite3.connect('../../../run/datastore/master.db', check_same_thread = False)
    cursor     = connection.cursor()
    cursor.execute("""SELECT username FROM users;""")
    username = cursor.fetchone()[0]
    log.append(username)
    cursor.execute("""SELECT password FROM users;""")
    password = cursor.fetchone()[0]
    log.append(password)
    return log

@omnibus.route('/login', methods=['GET', 'POST'])
def show_login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        log = users()
        print(log)
        username = request.form['username']
        password = request.form['password']
        if username == log[0]:
            if password == log[1]:
                return render_template('login.html')
        else:
            return render_template('login.html', message='Error: Bad Credentials')