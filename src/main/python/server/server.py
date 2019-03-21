"""

.. module:: site
   :synopsis: Restful User-Service outgoing point
.. moduleauthor:: Ecevit Emre Okan <github.com/eecevit-tgm>

"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse, abort, Api, Resource
import json
import hashlib

app = Flask(__name__)
CORS(app)
api = Api(app)
auth = HTTPBasicAuth()

"""
==============================
||       READ  USERS        ||
==============================
"""

"""
Lieset die Daten aus dem JSON File heraus
"""

with open('user.json', 'r') as f:
    users = json.load(f)


def reader():
    """
    Returns the User in the file
    :return: the list of the user in the user.json file
    """
    return users


def writer(user):
    """
    Writes the users into the JSON File
    :param user: the users dict
    """
    users = user
    with open('user.json', 'w') as f:
        f.write(json.dumps(users))


"""
==============================
||     END READ  USERS      ||
==============================
"""
"""
==============================
||       HASHING  PW        ||
==============================
"""


def hash_password(password):
    pw_hash = hashlib.sha256(password.encode('utf-8'))
    dig = pw_hash.hexdigest()
    return dig


def verify_password(password, username):
    for user in USERS:
        if username == user['username']:
            password_hash = user['password']
            if hash_password(password) == password_hash:
                return True
            else:
                return False


"""
==============================
||    End of HASHING PW     ||
==============================
"""
USERS = reader()


def abort_if_user_doesnt_exist(username):
    """
    Check if user exists
    :param usernmane: username
    :return: User doesn't exist error in JSONs
    """
    position = 0
    for user in USERS:
        if username == user['username']:
            return position
        position += 1
    return -1
    #return False
    # abort(404, message="User {} doesn't exist")  # .format(username))


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('picture')
parser.add_argument('password')
parser.add_argument('admin')


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    for user in USERS:
        if user['username'] == username:
            if verify_password(password, username):
                checkAdmin(username)
                return True


def checkAdmin(username):
    pos = abort_if_user_doesnt_exist(username)
    if USERS[pos]['admin'] == "true":
        return True
    else:
        return False


# Todo
# shows a single todo item and lets you delete a todo item

class Admin(Resource):
    def get(self, username):
        pos = abort_if_user_doesnt_exist(username)
        return [USERS[pos]['admin']]


class Todo(Resource):

    @auth.login_required
    def get(self, username):
        """
        **Get information of a specific user**

        This function allows user to get a specific user's information through their username.
        :param username: id of the teacher
        :return: user's information accessed by user in json and http status code
        - Example::
            curl http://127.0.0.1:5000/user/eecevit
        - Expected Success Response::
             {
             "id": "1",
             "username": "eecevit",
             "email": "eecevit@student.tgm.ac.at"
             "picture":"..."
             }
        - Expected Fail Response::
            HTTP Status Code: 404

        """
        pos = abort_if_user_doesnt_exist(username)
        return [USERS[pos]]

    @auth.login_required
    def delete(self, username):
        """
        **Delete User Record**

        This function allows user to delete a user record.

        :param username: name of the user
        :return: delete status in json and http status code

        - Example::
            curl http://127.0.0.1:5000/user/eecevit -X DELETE -v

        - Expected Success Response::
            HTTP Status Code: 204

        - Expected Fail Response::
            HTTP Status Code: 404
        """

        if checkAdmin(request.authorization["username"]):
            pos = abort_if_user_doesnt_exist(username)
            del USERS[pos]
            writer(USERS)
            return '', 204

    @auth.login_required
    def put(self, username):
        """
         **Update Information of a Specific User Record**
        This function allows user to update a specific users's information through their username.
        :param username: name of the user
        :return: users's information updated
        - Example::
            curl http://127.0.0.1:5000/user/eecevit -d "username=newName" -d"email=mail@mail.com" -d"picture=eecevit.jpg" -X PUT -v
        - Expected Success Response::
            HTTP Status Code: 201
            {
                "username": "newName",
                "email": "mail@mail.com",
                "picture": "....."
            }
        - Expected Fail Response::
            HTTP Status Code: 404
        """
        if checkAdmin(request.authorization["username"]):
            pos = abort_if_user_doesnt_exist(username)
            args = parser.parse_args()
            if args['password'] != USERS[pos]['password']:
                user = {'username': args['username'], 'email': args['email'], 'picture': args['picture'],
                        'password': hash_password(args['password']), 'admin': args['admin']}
            else:
                user = {'username': args['username'], 'email': args['email'], 'picture': args['picture'],
                        'password': args['password'], 'admin': args['admin']}
            USERS[pos] = user
            writer(USERS)
            return user, 201


class TodoList(Resource):

    @auth.login_required
    def get(self):
        """
              **Get List of Users**
                 This function allows users to get a list of users and their id, username, email and image.
                 :return: user's information in json and http status code
                 - Example::
                       curl http://localhost:5000/users -X GET -v
                 - Expected Success Response::
                     HTTP Status Code: 200
                     {
                         "eecevit": {"id": "1", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                         "danho": {"id": "2", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                         "dsunaric": {"id": "3", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."},
                         "elshal": {"id": "4", "username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "...."}
                     }
        """

        return USERS

    @auth.login_required
    def post(self):
        """
                 **Create User Record**
                 This function allows user to create(post) a user record.
                 :return: user's information added by the user in json
                 - Example::
                     curl http://localhost:5000/user -d "username=newName" -d"email=mail@mail.com" -d"eecevit.jpg" -X POST -v
                 - Expected Success Response::
                     HTTP Status Code: 201
                     {
                         "username": "newUser",
                         "email": "newUser@mail.at",
                         "picture": "....."
                     }
                 - Expected Fail Response::
                     HTTP Status Code: 400
        """
        args = parser.parse_args()
        user_id = len(USERS)
        USERS.append({'username': args['username'], 'email': args['email'], 'picture': args['picture'],
                      'password': hash_password(args['password']), 'admin': args['admin']})
        writer(USERS)
        return USERS[user_id], 201


class UserCheck(Resource):
    def get(self):
        return jsonify('OK')

    def post(self):
        args = parser.parse_args()
        pos = abort_if_user_doesnt_exist(args['username'])
        if pos >= 0:
            if USERS[pos]['password'] == hash_password(args['password']):
                return jsonify(True)
            else:
                return jsonify(False)


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/users')
api.add_resource(Todo, '/users/<username>')
api.add_resource(Admin, '/user/<username>')
api.add_resource(UserCheck, '/check')

if __name__ == '__main__':
    app.run()
