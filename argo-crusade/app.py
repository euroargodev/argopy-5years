#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template, url_for
import ast
import json
import os
import sys
import glob
import random
import string

sub_uri = os.getenv("SUB_URI", "/")

app = Flask(__name__, static_url_path=f'{sub_uri}/static')
# Set root folder and application name
ROOT = os.path.abspath(os.path.dirname(__file__))

@app.route(f"{sub_uri}/")
def init_webpage():
    """landing page routing function
    Render the index.html template
    """
    # Render index
    return render_template('index.html')


@app.route(f"{sub_uri}/savescore", methods=['POST', 'GET'])
def save_score():
    """routing function to save & display the scoreboard
    Read, append & save json scores file    
    Render the scoreboard.html template
    """
    username = request.args.get('username')
    score = request.args.get('score')
    listObj = []

    with open(os.path.join(ROOT, "static/scores.json"), mode='r', encoding='utf-8') as fp:
        listObj = json.load(fp)
        # Remove Duplicates
        listObj = [i for n, i in enumerate(listObj) if i not in listObj[n + 1:]]
        # Append
        listObj.append({
            "name": username,
            "score": score
        })
    with open(os.path.join(ROOT, "static/scores.json"), mode='w') as json_file:
        json.dump(listObj, json_file,   indent=4,
                  separators=(',', ': '))

    return "Score published"   

@app.route(f"{sub_uri}/scoreboard")
def scoreboard():    
    #Render Scoreboard
    return render_template('scoreboard.html')


if __name__ == '__main__':
    app.run()
