'''
Decrypto party game, online multiplayer version. Based on the work of
WhoaWhoa.
'''
import json
import os
import random
import string

import flask
import redis

DEFAULT_REDIS_URL = 'redis://localhost:6379/0'
EXPIRE = 60 * 60 * 24 * 30  # 30 days

app = flask.Flask(__name__)
r = redis.from_url(os.environ.get('REDIS_URL', DEFAULT_REDIS_URL))
with open('wordlist.txt') as f:
    wordlist = f.read().splitlines()


@app.route('/')
def index():
    team = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))
    words = random.sample(wordlist, 4)
    r.set(team, json.dumps(words), ex=EXPIRE)
    return flask.redirect(flask.url_for('team', team=team))


@app.route('/<team>')
def team(team):
    words = r.get(team)
    if words:
        words = json.loads(words)
        return flask.render_template('index.html', words=words)
    return flask.render_template('404.html'), 404
