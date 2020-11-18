#VolunTeach Tutoring Services

from Client import Client
from Tutor import Tutor
from flask import Flask, url_for, render_template, redirect, request, Blueprint
from collections import defaultdict
from datetime import datetime, time
from dateutil import tz
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/schedule', methods=('GET', 'POST'))
def display_match():   
    # tutors = mock_tutors_availabilities()

    #first attempt connected front end to back end
    #one small step for man one giant leap for volunteach
    #client1 = Client.getClient1()
    tutor1 = Tutor.getTutor1()
    tutor2 = Tutor.getTutor2()
    tutor3 = Tutor.getTutor3()
    possTutors = {
        tutor1.getEmail() : tutor1,
        tutor2.getEmail() : tutor2,
        tutor3.getEmail() : tutor3
    }

    data = "Success"

    #data = {}
    if request.method == "POST":
        data = request.get_json()
        timeRanges = data['schedule']
        client1 = Client.getClient1()
        client1.setName("Client 1")
        client1.setEmail("client1@volunteachtutoring.org")
        

        for range in timeRanges:
            # METHOD 1: Hardcode zones:
            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('America/Chicago')

            # utc = datetime.utcnow()
            utc0 = datetime.strptime(range[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            utc1 = datetime.strptime(range[1], '%Y-%m-%dT%H:%M:%S.%fZ')

            # Tell the datetime object that it's in UTC time zone since 
            # datetime objects are 'naive' by default
            utc0 = utc0.replace(tzinfo=from_zone)
            utc1 = utc1.replace(tzinfo=from_zone)

            # Convert time zone
            lowerBoundDT = utc0.astimezone(to_zone)
            upperBoundDT = utc1.astimezone(to_zone)

            #get the upper and lower bound times so they can be fed into a client schedule
            day = adjustDay(lowerBoundDT.weekday())
            lowerHour = lowerBoundDT.hour
            lowerMin = lowerBoundDT.minute
            lowerTime = lowerHour + (lowerMin / 60.0)
            upperHour = upperBoundDT.hour
            upperMin = upperBoundDT.minute
            upperTime = upperHour + (upperMin / 60.0)
            client1.setTimeSlot(day, lowerTime, upperTime, 1)
            print(day)
            print(lowerTime)
            print(upperTime)
        
        #build client object with this data
        #need to parse this data to get day of week and time ranges
        print(data)

    #client1 = Client.getClient1()
    
    matched_tutor = client1.bestTutor(possTutors, 2, 1)
    if (matched_tutor is None):
        print("NO MATCHED TUTORS")
        return  Tutor.nullJSON()

    print(" MATCHED WITH " + matched_tutor.getName())
    #return the JSON format of matched_tutor
    return matched_tutor.getJSON()
    #return JSON of tutor with time ranges
    
def adjustDay(dayOfWeek):
    return (dayOfWeek + 1) % 7
    


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

if __name__ == '__main__':
    app.run()