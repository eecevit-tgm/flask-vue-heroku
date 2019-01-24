import pytest

import server.server


@pytest.fixture
def client():
    server.server.app.testing = True
    client = server.server.app.test_client()
    yield client


def test_readall(client):
    res = client.get('/user')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"},{"username":  "dsunaric", "email":  "dsunaric@student.tgm.ac.at", "picture": "link"}]


def test_singleUser(client):
    res = client.get('/user/eecevit')
    assert res.json == [{"username": "eecevit", "email": "eecevit@student.tgm.ac.at", "picture": "ds"}]
