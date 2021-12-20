from flask import Flask, render_template,request

app = Flask(__name__)
mypath = '/static/img/'

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home_func():
    return render_template('home.html', title='Home')


@app.route('/about', methods=['GET', 'POST'])
def about_func():
    return render_template('about.html', title='About')

@app.route('/darkroom', methods=['GET', 'POST'])
def dark_func():
    return render_template('darkroom.html', title='Dark Room', photos=[mypath+'tree1.jpg',mypath+'storm1.jpg',mypath+'storm2.jpg',mypath+'storm3.jpg',mypath+'storm4.jpg',mypath+'bigBike.jpg',mypath+'smallBike.jpg',mypath+'truck.jpg',mypath+'fruits.jpg',mypath+'sax.jpg',mypath+'bookx.jpg'])


if __name__ == '__main__':
    app.run(debug=True)
