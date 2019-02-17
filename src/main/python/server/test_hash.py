import hashlib
import json

password_hash = ""

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
    hex_dig = pw_hash.hexdigest()
    return hex_dig


def verify_password(password):
    if hash_password(password) == password_hash:
        return True
    else:
        return False


USERS = reader()

if __name__ == '__main__':
    print(USERS)
