'''
Decrypto party game, online multiplayer version. Based on the work of
WhoaWhoa.
'''
import json
import os
import random
import pathlib
import string

import flask
import redis

WORDLISTS_DIR = pathlib.Path('wordlists')
DEFAULT_REDIS_URL = 'redis://localhost:6379/0'
EXPIRE = 60 * 60 * 24 * 30  # 30 days
LANGUAGES = {
    'eng': 'English',
    'heb': 'Hebrew',
}

app = flask.Flask(__name__)
r = redis.from_url(os.environ.get('REDIS_URL', DEFAULT_REDIS_URL))

wordlists = {}
for language in LANGUAGES:
    with open(WORDLISTS_DIR / language) as f:
        wordlists[language] = f.read().splitlines()


@app.route('/')
def index():
    language = flask.request.args.get('language', 'eng')
    team = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))
    words = random.sample(wordlists[language], 4)
    r.set(team, json.dumps(words), ex=EXPIRE)
    return flask.redirect(flask.url_for('team', team=team))


@app.route('/<team>')
def team(team):
    words = r.get(team)
    if words:
        words = json.loads(words)
        return flask.render_template(
            'index.html',
            words=words,
            languages=LANGUAGES,
        )
    return flask.render_template('404.html'), 404
