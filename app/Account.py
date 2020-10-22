#VolunTeach Tutoring Services

from abc import ABC, abstractclassmethod

#abstract class with subclasses Client and Tutor

class Account(ABC):

    #constructors
    def __init__(self):
        self.name = ""
        self.email = ""
        self.avail = [[0 for j in range(48)] for i in range(7)]
        super().__init__()

    def __init__(self, name, email, avail):
        self.name = name
        self.email = email
        self.avail = avail
        super().__init__()

    #setters
    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setAvail(self, avail):
        self.avail = avail

    #getters
    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getAvail(self):
        return self.avail    