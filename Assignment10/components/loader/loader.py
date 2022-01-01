from flask import Blueprint, render_template

# loader blueprint definition
loader = Blueprint('loader', __name__, static_folder='static', static_url_path='/loader', template_folder='templates')
