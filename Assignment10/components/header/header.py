from flask import Blueprint,session,redirect,url_for

# header blueprint definition
header = Blueprint('header', __name__, static_folder='static', static_url_path='/header', template_folder='templates')

@header.route('/resign')
def resign():
    session['username'] = ''
    return redirect(url_for('home_func'))