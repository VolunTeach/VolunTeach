#VolunTeach Tutoring Services

from abc import ABC, abstractclassmethod


#abstract class with subclasses Client and Tutor

class Account(ABC):

    #constructors
    def __init__(self):
        self.name = ""
        self.email = ""
        self.genAvail = [[0 for j in range(48)] for i in range(7)]
        self.curAvail = self.genAvail
        # self.subjects = Subjects()
        super().__init__()

    def __init__(self, name, email, genAvail):
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

    #day - day of the week (0 = Sunday, 6 = Saturday)
    #start - double representing the first 30 minute time slot to be included (0.0 = 12:00 AM, 20.5 = 8:30 PM)
    #end - double representing the first 30 minute time slot to not be included
    def setTimeSlot(self, day, start, end, value):
        start = start * 2
        end = end * 2
        for i in range(start, end):
            genAvail[day][i] = value

    



            