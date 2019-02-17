import hashlib
import json

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


def hash_password(password):
    pw_hash = hashlib.sha256(password)
    dig = pw_hash.hexdigest()
    return dig


def verify_password(password, username):
    for user in USERS:
        if username == user['username']:
            password_hash = user['password']
            if hash_password(password) == password_hash:
                return True
    return False


USERS = reader()

if __name__ == '__main__':
    print(verify_password(b'hallo', 'eecevit'))
