'''
Decrypto party game, online multiplayer version. Based on the work of
WhoaWhoa.
'''
from flask import Flask, render_template

app = Flask(__name__)
teams = {}  # team hash -> (starting_time, words)
with open('wordlist.txt') as f:
    words = f.read().splitlines()


@app.route('/')
def index():
    return render_template('index.html')
