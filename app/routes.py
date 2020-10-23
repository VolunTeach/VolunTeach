from app import app
from app.forms import MatchForm
from flask import Flask, url_for, render_template, redirect, request
from collections import defaultdict
from datetime import datetime, time

@app.route('/')
def home():
    return "Hello World"

"""
This URL shows a new client's available times and a dictionary of tutors. For now, these are hardcoded in
and are just here to serve the visual purpose of showing the times (also looks terrible, but fine for now).
Our scheduling algorithm will likely be a 48 x 7 boolean array and will have to be visually represented. 
For demonstration purposes just populate the boolean array with values that correspond to the hardcoded availabilities.
"""
@app.route('/available', methods=('GET', 'POST'))
def display_availabilities():
    form = MatchForm()
    client = mock_client_availabilities()
    tutors = mock_tutors_availabilities()
    if request.method == 'POST':
        return redirect(url_for('display_match'))

    return render_template('available.jinja2', client=client, tutors=tutors, form=form, template='form-template')

@app.route('/display_match', methods=('GET', 'POST'))
def display_match():
    client = mock_client_availabilities()
    tutors = mock_tutors_availabilities()
    matched_tutor = 'Tutor 1'
    return render_template('matches.jinja2', matched_tutor=matched_tutor, tutors=tutors)

def mock_client_availabilities():
    client = []

    for i in range(1, 12, 3):
        cur_range = [None]*2
        start = time(hour=i, minute=0, second=0)
        end = time(hour=i+1, minute=0, second=0)
        cur_range[0] = str(start)
        cur_range[1] = str(end)
        client.append(cur_range)
    
    return client

def mock_tutors_availabilities():
    tutors = defaultdict(list)

    for i in range(1, 12, 3):
        cur_range = [None]*2
        start = time(hour=i, minute=0, second=0)
        end = time(hour=i+2, minute=0, second=0)
        cur_range[0] = str(start)
        cur_range[1] = str(end)
        tutors['Tutor 1'].append(cur_range)
    
    for i in range(1, 12, 4):
        cur_range = [None]*2
        start = time(hour=i, minute=0, second=0)
        end = time(hour=i+1, minute=0, second=0)
        cur_range[0] = str(start)
        cur_range[1] = str(end)
        tutors['Tutor 2'].append(cur_range)
    
    tutors['Tutor 3'].append(['01:00:00', '05:00:00'])

    return tutors
