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


    def bestTutor(self, possTutors, subject, duration, frequency):
        max = 0
        for email in possTutors:
            tutAvail = possTutors[email].getGenAvail()
            currCount = 0
            #counting the number of potential session windows between the client and tutor based off genAvail
            for i in range(len(tutAvail)):
                for j in range(len(tutAvail[i])):
                    if tutAvail[i][j] and self.genAvail[i][j]:
                        consec = 1
                        #if the count does not seem right, double check this for loop
                        #this counts the number of consecutive 30 minute time blocks are available starting at the current position
                        for k in range(len(tutAvail[i]) - 1 - j):
                            if tutAvail[i][j+k] and self.getAvail[i][j+k]:
                                consec += 1
                            else:
                                break
                        #if this window of time is at least the length of the duration, the total count for the tutor increases
                        if consec >= duration:
                            currCount += 1
            #decision for review is if this should be >= or just >
            if currCount >= max:
                max = currCount
                bestTutor = possTutors[email]
        #if there was a best tutor that could do ~frequency~ number of sessions, return the tutor
        #in the future it should configure in 
        if max >= frequency:
            return bestTutor
        else:
            return None