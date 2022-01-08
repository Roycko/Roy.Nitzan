from flask import Blueprint, render_template

# about blueprint definition
about = Blueprint('about', __name__, static_folder='static', static_url_path='/about', template_folder='templates')


# Routes
@about.route('/about', methods=['GET', 'POST'])
def about_func():
    return render_template('about.html', title='About')
