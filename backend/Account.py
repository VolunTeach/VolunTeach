#VolunTeach Tutoring Services

from abc import ABC, abstractclassmethod
import json

#abstract class with subclasses Client and Tutor

class Account(ABC):

    #constructors   

    def __init__(self, name = "", email = "", genAvail = [[0 for j in range(48)] for i in range(7)]):
        self.name = name
        self.email = email
        self.genAvail = genAvail
        self.curAvail = self.genAvail
        # self.subjects = Subjects()
        super().__init__()

    #setters
    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setGenAvail(self, genAvail):
        self.genAvail = genAvail

    def setCurAvail(self, curAvail):
        self.curAvail = curAvail

    #getters
    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getGenAvail(self):
        return self.genAvail

    def getCurAvail(self):
        return self.curAvail    

    #other methods

    #setTimeSlot
    #day - day of the week (0 = Sunday, 6 = Saturday)
    #start - double representing the first 30 minute time slot to be included (0.0 = 12:00 AM, 20.5 = 8:30 PM)
    #end - double representing the first 30 minute time slot to not be included
    def setTimeSlot(self, day, start, end, value):
        if (end > 23.5 and end < 24):
            end = 24.0
        start = int(start * 2)
        end = int(end * 2)
        for i in range(start, end):
            self.genAvail[day][i] = value

    #getJSON
    #returns a JSON serializable version of the name and schedule information
    def getJSON(self):
        accDict = {'name': 'You matched with ' + self.name}
        return json.dumps(accDict, indent = 4)



    



            