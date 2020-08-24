'''
Decrypto party game, online multiplayer version. Based on the work of
WhoaWhoa.
'''
import random
import string

import flask

app = flask.Flask(__name__)
teams = {}  # team hash -> words
with open('wordlist.txt') as f:
    wordlist = f.read().splitlines()


@app.route('/')
def index():
    team = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))
    words = random.sample(wordlist, 4)
    teams[team] = words
    return flask.redirect(flask.url_for('team', team=team))


@app.route('/<team>')
def team(team):
    words = teams.get(team)
    if words:
        return flask.render_template('index.html', words=words)
    return flask.render_template('404.html'), 404
