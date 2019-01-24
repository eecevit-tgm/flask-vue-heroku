from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


with open('user.json', 'r') as f:
    users = json.load(f)


def reader():
    return users


def delete(name):
    if name in users:
        users.pop(name)
    writer()


def create(name, id, email):
    users.update({name: {'id': id, 'username': name, 'email': email}})
    writer()


def writer(user):
    users = user
    with open('user.json', 'w') as f:
        f.write(json.dumps(users))


USERS = reader()


def abort_if_user_doesnt_exist(username):
    position = 0
    for user in USERS:
        if username in user['username']:
            return position
        else:
            abort(404, message="User {} doesn't exist")#.format(username))
        position += 1


parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('picture')


# Todo
# shows a single todo item and lets you     delete a todo item
class Todo(Resource):
    def get(self, username):
        pos = abort_if_user_doesnt_exist(username)
        return [USERS[pos]]

    def delete(self, username):
        abort_if_user_doesnt_exist(username)
        del USERS[username]
        delete(username)
        return '', 204

    def put(self, username):
        args = parser.parse_args()
        # name = args['user'].split(",")
        user = {'username': args['username'], 'email': args['email'], 'picture': args['picture']}
        USERS[username] = user
        return user, 201



class TodoList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        # user_id = int(max(USERS.keys()).lstrip('user')) + 1
        # user_id = 'user%i' % user_id
        user_id = len(USERS)
        USERS.append({'username': args['username'], 'email': args['email'], 'picture': args['picture']})
        writer(USERS)
        return USERS[user_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/users')
api.add_resource(Todo, '/users/<username>')

if __name__ == '__main__':
    app.run(debug=True)
