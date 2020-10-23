#VolunTeach Tutoring Services

from app.Account import Account

#this class inherits Account
class Client(Account):

    #constructors
    def __init__(self):
        super(Tutor, self).__init__()
        self.tutors = ""
        self.duration = 0

    def __init__(self, name, email, avail, subjects, tutors, duration):
        super(Tutor, self).__init__(name, email, avail)
        self.tutors = tutors
        self.duration = duration

    #setters    
    def setTutors(self, tutors):
        self.clients = clients
        
    def setDuration(self, duration):
        self.duration = duration

    #getters
    def getTutors(self):
        return self.tutors

    def getDuration(self):
        return self.duration

    #matching algorithm
    def match(self, possTutors):
        if not tutors:
            tutors = ""
            #implement main algorithm here
        else:
            return tutors
