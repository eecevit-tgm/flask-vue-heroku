
USERS = [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}, {"username": "dsunaric", "email": "dsunaric@student.tgm.ac.at", "picture": "link"}, {"username": "test", "email": "wow", "picture": "www-X"}, {"username": "Jack", "email": "programmer", "picture": "asdasd"}, {"username": "tip", "email": "top", "picture": "moruk"}]

username = "tip"
position = 0
realpos = 0
for user in USERS:
    if username is user['username']:
        print("mal was neues")
        realpos = position
    position += 1
if USERS[realpos]['username'] is username:
    print('geht')
else:
    print("geht ned")