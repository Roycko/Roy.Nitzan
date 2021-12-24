from flask import Flask, render_template,request,session,redirect,url_for

app = Flask(__name__)
app.secret_key ='123'

mypath = '/static/img/'

@app.route('/resign')
def resign():
    session['username'] = ''
    return redirect(url_for('home_func'))
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

@app.route('/assignment9', methods= ['GET','POST'])
def ass9_func():
    users = {'user1' : {'name' : 'roy', 'email' : 'roy@assignment9.com'},'user2' : {'name' : 'shabi', 'email' : 'Shabi@assignment9.com'},'user3' : {'name' : 'tutti', 'email' : 'tutti@assignment9.com'},'user4' : {'name' : 'moti', 'email' : 'Moti@assignment9.com'},'user5' : {'name' : 'yakov', 'email' : 'yakov@assignment9.com'}}
    usersLen= len(users)
    if request.method == 'GET':
        if request.args.get('user') or  request.args.get('email'):
            username = request.args['user'].lower()
            email = request.args['email'].lower()
            for k,v in users.items():
                if v.get('name') == username or v.get('email') == email:
                    print ('Username = ',v.get('name') , ', Email = ', v.get('email'))
                    return render_template('Assignment9.html', title='assignment 9', username=v.get('name'), email=v.get('email'))
        if request.args.get('user') =='' and request.args.get('email')=='':
            return render_template('Assignment9.html', title='assignment 9',users=users)

    elif request.method == 'POST' and request.form['user2'] != '' and request.form['email2'] != '':
        session['username'] = request.form['user2']
        newUser = 'user'+str(usersLen+1)
        users.update ({newUser : {'name' :request.form['user2'] , 'email': request.form['email2']}})
    return render_template('Assignment9.html', title='assignment 9')



if __name__ == '__main__':
    app.run(debug=True)
