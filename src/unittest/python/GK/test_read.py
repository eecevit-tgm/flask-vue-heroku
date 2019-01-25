import pytest
import server.server


user01 = {"username":"test01", "email":"test01@student.tgm.ac.at", "picture":"Tester0123"}
user02 = {"username":"test02", "email":"test02@student.tgm.ac.at", "picture":"Tester0123"}
user03 = {"username":"test03", "email":"test03@student.tgm.ac.at", "picture":"Tester0123"}


@pytest.fixture
def client():
    server.server.app.testing = True
    client = server.server.app.test_client()
    yield client

@pytest.yield_fixture(autouse=True)
def run_around_tests():
    file = open('user.json', "w+")
    file.write('[{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]')

def test_delAllUsersStart(client):
    res = client.get("/users").json
    length = len(res)
    print(length)
    for tester in res:
        username = tester['username']
        client.delete("/users/"+username)
    res02 = client.get("users").json
    assert len(res02) == 0

def test_addStartUser(client):
    client.post("/users", json={"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"})
    res = client.get("/users/eecevit")
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]


def test_readAll(client):
    res = client.get('/users')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]


def test_singleUser(client):
    res = client.get('/users/eecevit')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]

def test_singleUser(client):
    client.post("/users", json=user01)
    res = client.get('/users/test01').json[0]
    assert (res['username'] == "test01") and (res['email'] == "test01@student.tgm.ac.at") and (res['picture'] == "Tester0123")
    client.delete("/users/test01")


def test_addUser(client):
    client.post("/users", json=user01)
    res = client.get("/users/test01")
    res02 = res.json[0]
    assert (res02['username'] == "test01") and (res02['email'] == "test01@student.tgm.ac.at") and (res02['picture'] == "Tester0123")
    client.delete("/users/test01")


def test_addMultiple(client):
    client.post("/users", json=user01)
    client.post("/users", json=user02)
    res01 = client.get("/users/test01").json[0]
    res02 = client.get("/users/test02").json[0]
    assert (res01['username'] == "test01") and (res01['email'] == "test01@student.tgm.ac.at") and (res01['picture'] == "Tester0123") and\
            (res02['username'] == "test02") and (res02['email'] == "test02@student.tgm.ac.at") and (res02['picture'] == "Tester0123")
    client.delete("/users/test01")
    client.delete("/users/test02")

def test_addMultiple02(client):
    client.post("/users", json=user01)
    client.post("/users", json=user02)
    client.post("/users", json=user03)
    res01 = client.get("/users/test01").json[0]
    res02 = client.get("/users/test02").json[0]
    res03 = client.get("/users/test03").json[0]
    assert (res01['username'] == "test01") and (res01['email'] == "test01@student.tgm.ac.at") and (res01['picture'] == "Tester0123") and\
            (res02['username'] == "test02") and (res02['email'] == "test02@student.tgm.ac.at") and (res02['picture'] == "Tester0123")and \
            (res03['username'] == "test03") and (res03['email'] == "test03@student.tgm.ac.at") and (res03['picture'] == "Tester0123")


def tes_delteMultiple02(client):
    client.delete("/users/test01")
    client.delete("/users/test02")
    client.delete("/users/test03")

    res01=client.get('/users/test01')
    res02=client.get('/users/test02')
    res03=client.get('/users/test03')

    assert b'{"message": "User {} doesn\'t exist"}\n' in res01.data and b'{"message": "User {} doesn\'t exist"}\n' in res02.data and b'{"message": "User {} doesn\'t exist"}\n' in res03.data


def test_updateUser(client):
    client.put('/users/eecevit', json=user02)
    res = client.get('/users/test02')
    res02 = res.json[0]
    assert (res02['username'] == "test02") and (res02['email'] == "test02@student.tgm.ac.at") and (res02['picture'] == "Tester0123")

def test_deleteUser(client):
    client.delete('/users/eecevit')
    res=client.get('/users/eecevit')
    print(res.data)
    assert b'{"message": "User {} doesn\'t exist"}\n' in res.data

def test_deleteUser02(client):
    client.post("/users", json=user01)
    client.delete("/users/user01")
    res = client.get("/users")
    print(res.data)

