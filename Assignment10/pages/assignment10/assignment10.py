from flask import Blueprint, render_template,request, redirect,flash,url_for
from interact_with_DB import interact_db
# assignment10 blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')
import mysql.connector

# Routes
@assignment10.route('/assignment10')
def ass10_func():
    query = "Select * from Users;"
    users= interact_db(query=query , query_type= "fetch")
    return render_template('assignment10.html', users=users)

@assignment10.route('/insert_user', methods=['POST'])
def insertUser():
    name = request.form['name']
    email = request.form['email']
    query2="select * from Users where email='%s';" % (email)
    numOfUsers = interact_db(query=query2,query_type="fetch")
    if len(numOfUsers)==0:
        query = "Insert into users (name, email) VALUES ('%s','%s');" % (name, email)
        interact_db(query=query, query_type="commit")
        flash(message="You have just added a user successfully !")
    else:
        flash(message="This Email address is already in the system!")
    return redirect('/assignment10')

@assignment10.route('/update_user', methods=['POST'])
def updateUser():
    name = request.form['name']
    email = request.form['email']
    query2="select * from Users where email='%s';" % (email)
    numOfUsers = interact_db(query=query2 , query_type= "fetch")
    if len(numOfUsers) != 0:
        query = "Update Users set name = '%s' where email='%s'" % (name, email)
        interact_db(query=query, query_type="commit")
        flash(message="You have just updated a user successfully !")
    else:
        flash(message="This Email address is NOT in the system!")
    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['POST'])
def deleteUser():
    email = request.form['email']
    query2="select name from Users where email='%s';" % (email)
    numOfUsers = interact_db(query=query2,query_type="fetch")
    if len(numOfUsers)!=0:
        query = "delete from Users where email='%s'" % (email)
        interact_db(query=query, query_type="commit")
        flash(message="The user was deleted from DB!")
    else:
        flash(message="This Email address is NOT in the system!")
    return redirect('/assignment10')
