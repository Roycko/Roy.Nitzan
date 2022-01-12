from flask import Blueprint, render_template,request, redirect,flash,url_for
from interact_with_DB import interact_db
import mysql.connector
import collections
from flask import jsonify
import json
import requests
# assignment12 blueprint definition
assignment12 = Blueprint('assignment12', __name__, static_folder='assignment12', static_url_path='/static', template_folder='templates')


@assignment12.route('/assignment12/restapi_users', defaults ={'user_id': 1})
@assignment12.route('/assignment12/restapi_users/<int:user_id>')
def ass12_user_func(user_id):
    query = f"select * from Users where id = {user_id};"
    users = interact_db(query,"fetch")
    if len(users) ==0:
        returned_json= {
           'Status':'Failed',
           'Error':'There is no User with that ID'
        }
    else:
        user = {
            'id': users[0].id,
            'name':users[0].name,
            'email':users[0].email
        }
        returned_json=json.dumps(user)
    return render_template('assignment12.html',users = returned_json)



# @assignment12.route('/assignment12/users')
# @assignment12.route('/assignment12')
# def ass12_users_func():
#     query = "Select * from Users;"
#     users_list = []
#     for row in interact_db(query,"fetch"):
#         d = collections.OrderedDict()
#         d['id'] = row[0]
#         d['name'] = row[1]
#         d['email'] = row[2]
#         d['create_date'] = row[3]
#         users_list.append(d)
#     users = json.dumps(users_list,default=str)
#     return render_template('assignment12.html', users=users)
#
#
# @assignment12.route('/assignment12/outer_source')
# def ass12_outerUsers_func():
#     id = 1
#     if "id" in request.args:
#         id = int(request.args['id'])
#     user = requests.get(f'https://reqres.in/api/users/{id}',verify = False)
#     print(user)
#     user = user.json()
#     print(user)
#     return render_template('assignment12.html', user=user)
