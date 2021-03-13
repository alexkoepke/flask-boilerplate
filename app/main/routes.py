from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_babel import _, get_locale
# from app.translate import translate
from app.main import bp
import requests


# index page
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title=_('Home'))


# index page
@bp.route('/catalog', methods=['GET', 'POST'])
def catalog():
    return render_template('index.html', title=_('Home'))
