#!/usr/bin/env python3

from flask import Blueprint, render_template, request, redirect


controller = Blueprint('general', __name__, url_prefix='/')


@controller.route('/', methods=['GET', 'POST'])
def show_frontpage():
    if request.method == 'GET':
        print('GET!!!')
        return render_template('search.html')
    else:
        print('POST!!!')
        redir = request.form['search']
        print(redir)
        return redirect('/{redir}'.format(redir=redir))

