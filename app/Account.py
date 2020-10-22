#VolunTeach Tutoring Services

from abc import ABC, abstractclassmethod
from app.Subjects import Subjects

#abstract class with subclasses Client and Tutor

class Account(ABC):

    #constructors
    def __init__(self):
        self.name = ""
        self.email = ""
        self.genAvail = [[0 for j in range(48)] for i in range(7)]
        self.curAvail = self.genAvail
        self.subjects = Subjects()
        super().__init__()

    def __init__(self, name, email, genAvail):
        self.name = name
        self.email = email
        self.genAvail = genAvail
        self.curAvail = self.genAvail
        self.subjects = Subjects()
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