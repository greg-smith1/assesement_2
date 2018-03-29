#!/usr/bin/env python3

from flask import Blueprint, render_template


controller = Blueprint('bicycle', __name__, url_prefix='/bicycle')


@controller.route('/', methods=['GET'])
def show_bicycle():
    return render_template('bicycle.html')
