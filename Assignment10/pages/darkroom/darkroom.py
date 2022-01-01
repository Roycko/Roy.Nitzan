from flask import Blueprint, render_template

mypath = '/static/img/'

# catalog blueprint definition
darkroom = Blueprint('darkroom', __name__, static_folder='static', static_url_path='/darkroom', template_folder='templates')


# Routes
@darkroom.route('/darkroom', methods=['GET', 'POST'])
def dark_func():

    return render_template('darkroom.html', title='Dark Room', photos=[mypath+'tree1.jpg',mypath+'storm1.jpg',mypath+'storm2.jpg',mypath+'storm3.jpg',mypath+'storm4.jpg',mypath+'bigBike.jpg',mypath+'smallBike.jpg',mypath+'truck.jpg',mypath+'fruits.jpg',mypath+'sax.jpg',mypath+'bookx.jpg'])
