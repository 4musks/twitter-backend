from datetime import datetime
import random as rand

import pytest
import json
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()



def test_send_tweet_for_bad_id(app, client):
    res = client.post('/sendTweet?id=rerseresr')
    assert res.status_code == 400


def test_failure_with_bad_route(app, client):
    res = client.get('/')
    assert res.status_code == 404


def test_good_path(app, client):
    test = rand.random()
    res = client.post('/sendTweet?text=' + str(test))
    assert res.status_code == 200
    parsed = json.loads(res.data)

    res = client.get('/getTweet?id=' + str(parsed['id']))
    assert res.status_code == 200

    res = client.delete('/deleteTweet?id=' + str(parsed['id']))
    assert res.status_code == 200
