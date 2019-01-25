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

def test_readall(client):
    res = client.get('/users')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]


def test_singleUser(client):
    res = client.get('/users/eecevit')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]

def test_addUser(client):
    client.post("users", json=user01)
    res = client.get("/users/test01")
    print(res.data)
    assert (res.json['username'] == "test01") and (res.json['email'] == "test01@student.tgm.ac.at") and (res.json['picture'] == "Tester0123")


def test_update_user(client):
    client.put('/users/eecevit', json=user02)
    res = client.get('/users/eecevit')
    assert b'{"username":"test02", "email":"test02@student.tgm.ac.at", "picture":"Tester0123"}\n' in res.data

def test_delete_user(client):
    client.delete('/users/eecevit')
    res=client.get('/users/eecevit')
    assert b'{"message": "User {} doesn\'t exist.' in res.data