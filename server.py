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
    return flask.render_template('index.html')


@app.route('/new-team')
def new_team():
    team = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))
    words = random.sample(wordlist, 4)
    teams[team] = words
    return {'team': team, 'words': words}


@app.route('/get-team')
def get_team():
    team = flask.request.args.get("team")
    return {'words': teams[team]}
