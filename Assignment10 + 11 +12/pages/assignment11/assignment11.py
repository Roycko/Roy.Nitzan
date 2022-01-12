from flask import Blueprint, render_template,request, redirect,flash,url_for
from interact_with_DB import interact_db
import mysql.connector
import collections
import json
import requests
# assignment11 blueprint definition
assignment11 = Blueprint('assignment11', __name__, static_folder='assignment11', static_url_path='/static', template_folder='templates')



@assignment11.route('/assignment11/users')
@assignment11.route('/assignment11')
def ass11_users_func():
    query = "Select * from Users;"
    users_list = []
    for row in interact_db(query,"fetch"):
        d = collections.OrderedDict()
        d['id'] = row[0]
        d['name'] = row[1]
        d['email'] = row[2]
        d['create_date'] = row[3]
        users_list.append(d)
    users = json.dumps(users_list,default=str)
    return render_template('assignment11.html', users=users)


@assignment11.route('/assignment11/outer_source')
def ass11_outerUsers_func():
    id = 1
    if "id" in request.args:
        id = int(request.args['id'])
    user = requests.get(f'https://reqres.in/api/users/{id}',verify = False)
    print(user)
    user = user.json()
    print(user)
    return render_template('assignment11.html', user=user)
