from Account import Account
import logging

class Client(Account):
    
    def __init__(self):
        super().__init__()
        self.tutors = {}

    def __init__(self, name, email, avail, subjects, tutors):
        super().__init__(name, email, avail)
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


    def bestTutor(self, possTutors, duration, frequency):
        max = 0
        maxDays = 0
        for email in possTutors:
            tutAvail = possTutors[email].getGenAvail()
            print("*************************\n\n\n")
            print(tutAvail[0][0])
            print("**********************")
            currCount = 0
            daysOfWeek = 0
            #counting the number of potential session windows between the client and tutor based off genAvail
            for i in range(7):
                availToday = False
                for j in range(48):
                    if tutAvail[i][j] and self.genAvail[i][j]:
                        consec = 1
                        #if the count does not seem right, double check this for loop
                        #this counts the number of consecutive 30 minute time blocks are available starting at the current position
                        for k in range(48 - 1 - j):
                            if tutAvail[i][j+k] and self.genAvail[i][j+k]:
                                consec += 1
                            else:
                                break
                        #if this window of time is at least the length of the duration, the total count for the tutor increases
                        if consec >= duration:
                            currCount += 1
                            availToday = True
                #daysofweek and availToday handle the logic for counting the days of the week they are available
                if availToday:
                    daysOfWeek += 1
            #decision for review is if this should be >= or just >
            if currCount >= max:
                max = currCount
                bestTutor = possTutors[email]
                maxDays = daysOfWeek

        #if there was a best tutor that could do ~frequency~ number of sessions per week assuming one session per day max, return the tutor
        #in the future it should configure in 
        if maxDays >= frequency:
            return bestTutor
        else:
            return None 

    @staticmethod
    def getClient1():
        avail1 = [[0 for j in range(48)] for i in range(7)]
        for i in range(len(avail1)):
            for j in range(26, 28):
                avail1[i][j] = 1
            for k in range(32, 34):
                avail1[i][k] = 1
            for l in range(38, 40):
                avail1[i][l] = 1
            for m in range(44, 46):
                avail1[i][m] = 1
        return Client("Client 1", "client1@volunteachtutoring.org", avail1, "Algebra", None)