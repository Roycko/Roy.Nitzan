from flask import Blueprint, render_template, redirect, url_for

# home blueprint definition
home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


# Routes
@home.route('/home', methods=['GET', 'POST'])
@home.route('/', methods=['GET', 'POST'])
def home_func():
    return render_template('home.html', title='Home')