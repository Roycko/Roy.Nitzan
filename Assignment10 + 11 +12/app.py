from flask import Flask
from interact_with_DB import interact_db

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key='333'

###### Pages
## Homepage
from pages.home.home import home
app.register_blueprint(home)

## About
from pages.about.about import about
app.register_blueprint(about)

## Darkroom
from pages.darkroom.darkroom import darkroom
app.register_blueprint(darkroom)

## Assignment9
from pages.assignment9.assignment9 import assignment9
app.register_blueprint(assignment9)

## Assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

## Assignment11
from pages.assignment11.assignment11 import assignment11
app.register_blueprint(assignment11)

## Assignment12
from pages.assignment12.assignment12 import assignment12
app.register_blueprint(assignment12)

###### Components
## Header
from components.header.header import header
app.register_blueprint(header)

## Footer
from components.footer.footer import footer
app.register_blueprint(footer)

## Loader
from components.loader.loader import loader
app.register_blueprint(loader)


if __name__ == '__main__':
    app.run(debug=True)

