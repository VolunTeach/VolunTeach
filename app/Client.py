from app.Account import Account
import logging

class Client(Account):
    
    def __init__(self):
        super().__init__()
        self.tutors = {}

    def __init__(self, name, email, avail, subjects, tutors):
        super().__init__(name, email, avail, subjects)
        self.tutors = tutors
        
    def getTutors(self):
        return self.tutors

    def setTutors(self, tutors):
        self.tutors = tutors

    def addTutor(self, tutor):
        if not self.tutors.has_key(tutor.email):
            tutors[tutor.email] = tutor
        
        else:
            logging.info("Tutor " + tutor.email + "was unable to be added to list. Reason: Email already exists in client list")

    def removeTutor(self, tutor):
        self.tutors.pop(tutor.email)