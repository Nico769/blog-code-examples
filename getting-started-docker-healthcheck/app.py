from flask import Flask
import os

app = Flask(__name__)

has_killswitch_tripped = False

@app.route("/killswitch")
def killswitch():
    global has_killswitch_tripped
    has_killswitch_tripped = True

@app.route('/ping')
def ping():
    if has_killswitch_tripped:
        return ('', 500)
    return ('', 200)