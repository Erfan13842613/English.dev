from flask import render_template, request, make_response, url_for, redirect, flash, Blueprint

base = Blueprint('base', __name__)


@base.route('/')
@base.route('/home')
def Home():
    return render_template('index.html')


@base.route('/about_me')
@base.route('/home/about_me')
def About_Me():
    return render_template('About_Me.html')


@base.route('/license')
@base.route('/home/license')
def License():
    return render_template('License.html')
